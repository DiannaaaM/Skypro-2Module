import logging
import os
from logging import Logger
from typing import Any

if os.path.isfile(os.path.join("../src/src.logger.log")):
    os.remove(os.path.join("../src/src.logger.log"))


def setup_logging() -> Logger:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", encoding="utf-8")
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("app.log", mode="w")
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
