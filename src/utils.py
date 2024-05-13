import json
import logging
import os
from datetime import datetime
from typing import Any, Dict

import requests
from dotenv import load_dotenv

from src.external_api import get_currency_rate
from src.logger import setup_logging_for_utils

logger = setup_logging_for_utils()
logger.info("Application from utils starts....")

logger.info("Running 'read_json_file' function")


def read_json_file(file_name: str) -> Any:
    """
    Читает json файл и возвращает данные в виде словаря
    """
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        else:
            return []
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []


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
    return total


logger.info(f"End 'sum_amount' function \n\tReturn: {sum_amount}")
logger.info("Application from utils finished")
# logger = logging.getLogger(__name__)
# file_handler = logging.FileHandler("utils.log")
# file_formatter = logging.Formatter("%(asctime)s %(module)s \n\t%(levelname)s: %(message)s")
# file_handler.setFormatter(file_formatter)
# logger.addHandler(file_handler)
#
# logger.setLevel(logging.INFO)
#
# logger.info("SUCCESSFUL OPERATION")
