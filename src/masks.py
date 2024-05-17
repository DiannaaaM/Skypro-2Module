import logging
import os

from src.logger import setup_logging

logger = setup_logging()


def mask_card(number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    if len(number) == 16:
        masked_number = number[:4] + " " + number[4:6] + "** **** " + number[-4:]
        logger.info("Функция mask_card выполнена успешно")
        return masked_number
    else:
        logger.error("С функцией mask_card что-то пошло не так")
    return number


def mask_account(number: str) -> str:
    """Функция принимает на вход номер счёта и возвращает его маску."""
    if len(number) == 21:
        masked_number = "**" + number[-4:]
        logger.info("Функция mask_account выполнена успешно")
        return masked_number
    else:
        logger.error("С функцией mask_account что-то пошло не так")
    return number


if __name__ == "__main__":
    mask_card("1234567890123456")
    mask_account("12345678901234567890123456789012")
