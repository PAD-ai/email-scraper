"""A dedicated place to define any loggers we might use in main"""
import logging

from src.config import BaseConfig
from src.logger_class import StreamAndMongoLogger

logger = StreamAndMongoLogger(
    name="EmailScraper",
    log_file=BaseConfig.LOG_FILE,
    max_bytes=BaseConfig.LOG_FILE_SIZE * 1024 * 1024 * 5,
    backup_count=3,
    level=logging.DEBUG,
    mongo_uri=False,
    mongo_col="etl",
)
