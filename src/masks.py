import logging
import os


def mask_card(number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    if len(number) == 16:
        return number[:4] + " " + number[4:6] + "** **** " + number[-4:]
    return number


def mask_account(number: str) -> str:
    """Функция принимает на вход номер счёта и возвращает его маску."""
    if len(number) == 21:
        return "**" + number[-4:]
    return number


if os.path.isfile(os.path.join("../src/masks.log")):
    os.remove(os.path.join("../src/masks.log"))

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("masks.log")
file_formatter = logging.Formatter("%(asctime)s %(module)s \n\t%(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

logger.setLevel(logging.INFO)

logger.info("SUCCESSFUL OPERATION")
