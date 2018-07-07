import logging


class Logger:
    def __init__(self, level):
        self.level = level

    def get_logger(self, name):
        logging.basicConfig(format='%(asctime)s [%(levelname)s] %(name)s: %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
        logger = logging.getLogger(name)
        logger.setLevel(self.level)
        return logger
