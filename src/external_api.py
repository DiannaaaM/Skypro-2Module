import json
import logging
import os
from datetime import datetime
from typing import Any, Dict

import requests
from dotenv import load_dotenv

from src.logger import setup_logging

logger = setup_logging()

load_dotenv()

API_KEY = os.getenv("API_KEY")

import json
import logging
import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

from src.logger import setup_logging

logger = setup_logging()

load_dotenv()

API_KEY = os.getenv("API_KEY")


def get_currency_rate(currency: Any) -> Any:
    """Получает курс валюты от API и возвращает его в виде float"""
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"
    response = requests.get(url, headers={"apikey": "RgcvuCoKJiBgqVod7PgrcSNPzdTt51jP"}, timeout=15)
    response_data = json.loads(response.text)
    rate = response_data["rates"]["RUB"]
    if rate:
        logging.info("Функция get_currency_rate выполнена успешно")
    else:
        logging.error("С функцией get_currency_rate что-то пошло не так: %(error)s")
    return rate
