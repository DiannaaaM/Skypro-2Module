import logging

logger = logging.getLogger("external_api")
console_handler = logging.StreamHandler()
console_formatter = logging.Formatter("\t%(module)s: %(asctime)s \n%(levelname)s - %(message)s\n")
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
