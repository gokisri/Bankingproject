import logging
import os

def custom_logger(log_level=logging.DEBUG):
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    if not logger.handlers:
        # Create logs folder if it doesn't exist
        os.makedirs("logs", exist_ok=True)
        file_handler = logging.FileHandler("logs/automation.log", mode='a')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
