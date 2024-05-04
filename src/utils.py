import json
import os
from datetime import datetime
from typing import Any
import requests
from dotenv import load_dotenv


def read_json_file(file_name: str) -> dict[Any, Any]:
    """
    Читает json файл и возвращает данные в виде словаря
    """
    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


file = os.path.abspath(os.path.join("..", "data", "operations.json"))
print(read_json_file(file))

load_dotenv()

API_KEY = os.getenv("API_KEY")


def get_currency_rate(currency: str) -> float:
    """Получает курс валюты от API и возвращает его в виде float"""
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"
    response = requests.get(url, headers={"apikey": API_KEY}, timeout=5)
    response_data = json.loads(response.text)
    rate = response_data["rates"]["RUB"]
    return rate


def sum_amount(transactions: dict) -> dict[Any, Any]:
    """Суммирует суммы всех транзакций"""
    total = 0.0
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == "RUB":
            total += float(transaction["operationAmount"]["amount"])
        elif transaction.get("operationAmount", {}).get("currency", {}).get("code") == "EUR":
            total += float(transaction["operationAmount"]["amount"]) * get_currency_rate("EUR")
        elif transaction.get("operationAmount", {}).get("currency", {}).get("code") == "USD":
            total += float(transaction["operationAmount"]["amount"]) * get_currency_rate("USD")
    return total


transactions = {
    "id": 957763565,
    "state": "EXECUTED",
    "date": "2019-01-05T00:52:30.108534",
    "operationAmount": {"amount": "87941.37", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Перевод со счета на счет",
    "from": "Счет 46363668439560358409",
    "to": "Счет 18889008294666828266",
}, {
    "id": 667307132,
    "state": "EXECUTED",
    "date": "2019-07-13T18:51:29.313309",
    "operationAmount": {"amount": "97853.86", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Перевод с карты на счет",
    "from": "Maestro 1308795367077170",
    "to": "Счет 96527012349577388612",
}

print(sum_amount(transactions))
