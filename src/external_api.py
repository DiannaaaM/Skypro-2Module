import json
import os
from datetime import datetime
from typing import Any, Dict

import requests
from dotenv import load_dotenv

from src.logger import setup_logging_for_external_API

logger = setup_logging_for_external_API()
logger.info("Application from utils starts....")

logger.info("Running 'get_currency_rate' function")
load_dotenv()

API_KEY = os.getenv("API_KEY")


def get_currency_rate(currency: Any) -> Any:
    """Получает курс валюты от API и возвращает его в виде float"""
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"
    response = requests.get(url, headers={"apikey": API_KEY}, timeout=15)
    response_data = json.loads(response.text)
    rate = response_data["rates"]["RUB"]
    return rate


logger.info("End 'get_currency_rate' function")
logger.info("Application from utils finished")
