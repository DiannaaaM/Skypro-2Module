import json
import os
from datetime import datetime
from typing import Any, List

from src.convert_currncy import get_currency_rate


def sum_amount(transactions: List[dict]) -> float:
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


transactions = [
    {
        "id": 957763565,
        "state": "EXECUTED",
        "date": "2019-01-05T00:52:30.108534",
        "operationAmount": {"amount": "87941.37", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 46363668439560358409",
        "to": "Счет 18889008294666828266",
    }
]

print(sum_amount(transactions))
