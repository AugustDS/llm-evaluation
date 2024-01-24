import os
import logging
from datetime import datetime


class CustomLogger:
    def __init__(self):
        log_directory = "./logs"
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        log_filename = datetime.now().strftime("%Y-%m-%d") + ".log"
        log_filepath = os.path.join(log_directory, log_filename)

        self.logger = logging.getLogger('simple_logger')
        self.logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(log_filepath)
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    def log(self, level, message):
        if level.lower() == 'debug':
            self.logger.debug(message)
        elif level.lower() == 'info':
            self.logger.info(message)
        elif level.lower() == 'warning':
            self.logger.warning(message)
        elif level.lower() == 'error':
            self.logger.error(message)
        elif level.lower() == 'critical':
            self.logger.critical(message)
        else:
            raise ValueError(f"Invalid log level: {level}")
