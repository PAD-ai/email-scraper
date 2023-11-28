"""Email Collector class"""
from threading import Thread

from src.config import BaseConfig


class EmailOutput(Thread):
    """Email Collector Class"""

    def __init__(self, results):
        Thread.__init__(self)
        self.work = results

    def run(self):
        while True:
            title, emaillist = self.work.get()

            with open(BaseConfig.OUTPUT_FILE, "a", encoding="utf-8") as results_file:
                for email in emaillist:
                    results_file.write(f"{title}->{email}\n")

            self.work.task_done()
