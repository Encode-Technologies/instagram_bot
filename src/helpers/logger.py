import os
import logging

log_directory = "logs"

os.makedirs(log_directory, exist_ok=True)

def create_logger(name: str, log_level: int=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    #Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # File handler for logging to a file
    file_handler = logging.FileHandler(f'{log_directory}/app.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Console handler for printing logs to console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


logger = create_logger(__name__)