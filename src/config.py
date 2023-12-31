"""Configuration module for our Email Scraper"""
# pylint: disable=C0301,R0903
import datetime
import os


class BaseConfig:
    """Main configuration class"""

    now = datetime.datetime.now()
    date_string = now.strftime("%Y-%m-%d")
    time_string = now.strftime("%H-%M-%S")

    HOSTS_FILE = "domains.txt"
    THREADS_NUMBER = 20

    OUTPUT_FOLDER = "results"
    OUTPUT_FILE = f"{OUTPUT_FOLDER}/Results_{date_string}_{time_string}.txt"

    LOG_FOLDER = "logs"
    LOG_FILE = f"{LOG_FOLDER}/main.log"
    LOG_FILE_SIZE = 3

    REQUEST_TIMEOUT = 300
    HEADERS = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }
    EMAIL_PATTERN = r'(?:[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+(?:com|cat|es|org|net|eu|eus))'


if not os.path.exists(BaseConfig.LOG_FOLDER):
    os.makedirs(BaseConfig.LOG_FOLDER)
if not os.path.exists(BaseConfig.OUTPUT_FOLDER):
    os.makedirs(BaseConfig.OUTPUT_FOLDER)
