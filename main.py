"""Simple Email Scraper against a list of domains"""

import queue
import warnings

from src.config import BaseConfig
from src.loggers import logger
from src.results_class import EmailOutput
from src.scraper_class import DomainExplorer

# Ignore warnings because of verify=False on SSL certificates
warnings.filterwarnings("ignore")

if __name__ == "__main__":
    # Define two queues to work with. Set maxsize for the main queue
    domainqueue = queue.Queue(maxsize=5000)
    emailsqueue = queue.Queue()

    # Start our threads
    for _i in range(BaseConfig.THREADS_NUMBER):
        t = DomainExplorer(domainqueue, emailsqueue)
        t.daemon = True
        t.start()

    logger.info(f"Started {BaseConfig.THREADS_NUMBER} Threads")

    # Start our collector thread
    results_thread = EmailOutput(emailsqueue)
    results_thread.daemon = True
    results_thread.start()

    # Add domains to the queue from a context manager to save memory
    with open(BaseConfig.HOSTS_FILE, "r", encoding="utf-8") as domains_file:
        for domain in domains_file.readlines():
            domainqueue.put(domain.replace("\n", "").strip().split("->"))

    # Gracefully join our queues so that our threads can exit
    domainqueue.join()
    logger.info("Domains finished processing")
    emailsqueue.join()
    logger.info("Collector finished processing")
