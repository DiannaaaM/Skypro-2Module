import logging
import os
from logging import Logger
from typing import Any

if os.path.isfile(os.path.join("../src/src.logger.log")):
    os.remove(os.path.join("../src/src.logger.log"))


def setup_logging() -> Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(f"{logger}.log", mode="w")
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(module)s - %(levelname)s - %(message)s"))
    logger.addHandler(file_handler)

    return logger
