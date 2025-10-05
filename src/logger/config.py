import logging

default_formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
level_formatter = logging.Formatter('%(asctime)s - %(name)s -%(levelname)s - %(message)s')


class SingleLevelFilter(logging.Filter):
    def __init__(self, level):
        super().__init__()
        self.level = level

    def filter(self, record):
        return record.levelno == self.level


def setup_logger(name: str = 'app') -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # info logs handler
    info_handler = logging.FileHandler('./logs/app.log')
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(default_formatter)
    info_handler.addFilter(SingleLevelFilter(logging.INFO))

    # error logs handler
    error_handler = logging.FileHandler('./logs/app-error.log')
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(default_formatter)
    error_handler.addFilter(SingleLevelFilter(logging.ERROR))

    # debug handler
    debug_handler = logging.FileHandler('./logs/app-debug.log')
    debug_handler.setLevel(logging.DEBUG)
    debug_handler.setFormatter(level_formatter)
    # debug_handler.addFilter(SingleLevelFilter(logging.DEBUG)) Allow every level to come in here

    # for console logs
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(default_formatter)
    console_handler.setLevel(logging.DEBUG)

    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(info_handler)
        logger.addHandler(error_handler)
        logger.addHandler(debug_handler)

    return logger
