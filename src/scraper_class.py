"""
Main scraper class for a domain.
Visits each domain ad gets all the internal links on the homepage.
Then it checks each link for emails.
All emails found are added to a list and returned.
"""
# pylint: disable=C0103,R0902,W0718,W0201

import re
from threading import Thread

import requests
from bs4 import BeautifulSoup

from src.config import BaseConfig
from src.loggers import logger


class DomainExplorer(Thread):
    """A threading class that scrapes emails from domains"""

    def __init__(self, workerqueue, resultsqueue):
        Thread.__init__(self)
        self.work = workerqueue
        self.results = resultsqueue
        self.r = requests.Session()
        self.timeout = BaseConfig.REQUEST_TIMEOUT
        self.r.headers.update(BaseConfig.HEADERS)
        self.pattern = BaseConfig.EMAIL_PATTERN

    def run(self):
        while True:
            try:
                self.title, self.domain = self.work.get()
                self.main()
            except Exception as e:
                logger.error(str(e))
            finally:
                self.work.task_done()

    def main(self):
        """Main scraper function"""

        self.url = (
            self.domain if self.domain.startswith("http") else "http://" + self.domain
        )

        self.src = self.get_page_source()
        self.links = self.get_page_links()

        if self.url not in self.links:
            self.links.append(self.url)

        found_emails = self.get_emails()

        self.results.put((self.title, found_emails))

    def get_page_source(self):
        """A method to get the source code from a link"""

        response = self.r.get(self.url, timeout=self.timeout, verify=False)
        return response.text

    def get_page_links(self):
        """A method to scrape all the URLs from a page"""

        links = []
        self.soup = BeautifulSoup(self.src, "html.parser")
        if self.soup:
            for link in self.soup.find_all("a"):
                url = link.get("href")
                if self.domain in str(url) and url.startswith("http"):
                    links.append(link.get("href"))
                    # print(link.get('href'))

        return list(set(links))

    def get_emails(self):
        """A method to scrape emails from a page"""
        emails = []

        for link in self.links:
            try:
                response = self.r.get(link, timeout=self.timeout, verify=False)
                # print(link)
                emails2 = re.findall(self.pattern, response.text)
                for email in emails2:
                    if email not in emails and "/" not in email and "\\" not in email:
                        emails.append(email)
            except Exception as e:
                logger.error(f"{link} Didn't Process because: {e}")
                return list(set(emails))

        return list(set(emails))
