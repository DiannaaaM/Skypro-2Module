import logging
import os

from src.logger import setup_logging

logger = setup_logging()
logger.info("Application from utils starts....")
logger.info("Running 'mask_card' function")


def mask_card(number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    if len(number) == 16:
        return number[:4] + " " + number[4:6] + "** **** " + number[-4:]
    return number


logger.info("End 'mask_card' function")
logger.info("Running 'mask_account' function")


def mask_account(number: str) -> str:
    """Функция принимает на вход номер счёта и возвращает его маску."""
    if len(number) == 21:
        return "**" + number[-4:]
    return number


logger.info("End 'mask_account' function")
logger.info("Application from utils finished")
