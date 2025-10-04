import logging

default_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
default_level = logging.DEBUG


def setup_logger(name) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(default_level)

    # for console logs
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(default_formatter)
    console_handler.setLevel(default_level)

    # for file logs
    file_handler = logging.FileHandler('./logs/app.log', mode='a')
    file_handler.setFormatter(default_formatter)
    file_handler.setLevel(default_level)

    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
