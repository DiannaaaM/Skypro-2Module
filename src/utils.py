import json
import os
from datetime import datetime
from typing import Any, List

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


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


# file = os.path.abspath(os.path.join("..", "data", "operations.json"))
# print(read_json_file(file))


def get_currency_rate(currency: Any) -> Any:
    """Получает курс валюты от API и возвращает его в виде float"""
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"
    response = requests.get(url, headers={"apikey": API_KEY}, timeout=5)
    response_data = json.loads(response.text)
    rate = response_data["rates"]["RUB"]
    return rate


def sum_amount(transaction: List[dict]) -> float:
    """Суммирует суммы всех транзакций"""
    total = 0.0
    for t in transaction:
        if t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB":
            total += float(t["operationAmount"]["amount"])
        elif t.get("operationAmount", {}).get("currency", {}).get("code") == "EUR":
            total += float(t["operationAmount"]["amount"]) * get_currency_rate("EUR")
        elif t.get("operationAmount", {}).get("currency", {}).get("code") == "USD":
            total += float(t["operationAmount"]["amount"]) * get_currency_rate("USD")
    return total


# transactions = [
#     {
#         "id": 441945886,
#         "state": "EXECUTED",
#         "date": "2019-08-26T10:50:58.294041",
#         "operationAmount": {
#             "amount": "31957.58",
#             "currency": {
#                 "name": "руб.",
#                 "code": "RUB"
#             }
#         },
#         "description": "Перевод организации",
#         "from": "Maestro 1596837868705199",
#         "to": "Счет 64686473678894779589"
#     }
# ]
#
# print(sum_amount(transactions))
