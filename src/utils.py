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


def read_json_file(file_name: str) -> Any:
    """
    Читает json файл и возвращает данные в виде словаря
    """
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            data = json.load(f)
        logger.info("Функция read_json_file выполнена успешно".encode("utf-8"))
        return data
    except FileNotFoundError:
        logger.error("Файл не найден")
        return {}
    except json.decoder.JSONDecodeError:
        logger.error("Ошибка декодирования JSON")
        return {}


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
