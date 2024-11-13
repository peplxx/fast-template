from datetime import datetime
import os
import logging

from pydantic import BaseModel

from app.config import get_settings

class LoggingSettings(BaseModel):
    APP_NAME: str = get_settings().APP_NAME
    FILE_NAME: str = f"{APP_NAME}_{datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}.log"
    LOG_DIR: str = "logs"
    ENABLE_SQLALCHEMY_LOGGING: bool = True
    LOG_LEVEL: int = logging.DEBUG
    LOG_FORMAT: str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    DATE_FORMAT: str = '%Y-%m-%d %H:%M:%S'

logging_settings: LoggingSettings = LoggingSettings()


def setup_logging(logging_settings: LoggingSettings = logging_settings):
    if not os.path.exists(logging_settings.LOG_DIR):
        os.makedirs(logging_settings.LOG_DIR)

    # Set log file name with current date
    log_filename = os.path.join(logging_settings.LOG_DIR, logging_settings.FILE_NAME)


    # Basic configuration for logging
    logging.basicConfig(
        level=logging_settings.LOG_LEVEL,  # Set the logging level
        format=logging_settings.LOG_FORMAT,  # Log format
        datefmt=logging_settings.DATE_FORMAT,  # Date format
        handlers=[
            logging.FileHandler(log_filename),  # Log to a file
            logging.StreamHandler()  # Log to console
        ]
    )

    return logging.getLogger(logging_settings.APP_NAME)


__all__ = ["setup_logging", "logging_settings"]
