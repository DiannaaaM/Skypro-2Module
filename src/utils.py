import json
import logging
import os
from datetime import datetime
from typing import Any, Dict

import requests
from dotenv import load_dotenv

from src.external_api import get_currency_rate
from src.logger import setup_logging

logger = setup_logging()
logger.info("Application from utils starts....")

logger.info("Running 'read_json_file' function")


def read_json_file(file_name: str) -> Any:
    """
    Читает json файл и возвращает данные в виде словаря
    """
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            data = json.load(f)
        logging.info("Функция read_json_file выполнена успешно")
        return data
    except FileNotFoundError:
        logging.error("Файл не найден")
        return {}
    except json.decoder.JSONDecodeError:
        logging.error("Ошибка декодирования JSON")
        return {}


logger.info(f"End 'read_json_file' function \n\tReturn: {read_json_file}")
logger.info("Running 'sum_amount' function")


def sum_amount(transaction: dict) -> float:
    """Суммирует суммы всех транзакций"""
    total = 0.0
    if transaction.get("operationAmount", {}).get("currency", {}).get("code") == "RUB":
        total += float(transaction["operationAmount"]["amount"])
    elif transaction.get("operationAmount", {}).get("currency", {}).get("code") == "EUR":
        total += float(transaction["operationAmount"]["amount"]) * get_currency_rate("EUR")
    elif transaction.get("operationAmount", {}).get("currency", {}).get("code") == "USD":
        total += float(transaction["operationAmount"]["amount"]) * get_currency_rate("USD")
    if total:
        logging.info("Функция sum_amount выполнена успешно")
    else:
        logging.error("С функцией sum_amount что-то пошло не так: %(error)s")
    return total


logger.info(f"End 'sum_amount' function \n\tReturn: {sum_amount}")
logger.info("Application from utils finished")
