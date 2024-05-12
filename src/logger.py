import logging
import os
from typing import Any

if os.path.isfile(os.path.join("../src/utils.log")):
    os.remove(os.path.join("../src/utils.log"))
if os.path.isfile(os.path.join("../src/masks.log")):
    os.remove(os.path.join("../src/masks.log"))
if os.path.isfile(os.path.join("../src/external_API.log")):
    os.remove(os.path.join("../src/external_API.log"))


def setup_logging_for_utils() -> Any:
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler("utils.log")
    logger.addHandler(file_handler)
    file_formatter = logging.Formatter("%(asctime)s %(module)s %(levelname)s: %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.setLevel(logging.INFO)
    return logger


def setup_logging_for_masks() -> Any:
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler("masks.log")
    logger.addHandler(file_handler)
    file_formatter = logging.Formatter("%(asctime)s %(module)s %(levelname)s: %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.setLevel(logging.INFO)
    return logger


def setup_logging_for_external_API() -> Any:
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler("external_API.log")
    logger.addHandler(file_handler)
    file_formatter = logging.Formatter("%(asctime)s %(module)s %(levelname)s: %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.setLevel(logging.INFO)
    return logger
