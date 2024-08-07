import json
import os
from typing import Any, List
from unittest.mock import Mock, patch

import pytest

from src.utils import get_currency_rate, read_json_file, sum_amount


@pytest.fixture()
def path_to_json_file() -> str:
    file = os.path.abspath(os.path.join("..", "data", "operations.json"))
    return file


@patch("builtins.open", create=True)
def test_read_file(mock_open: Any, path_to_json_file: str) -> None:
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = "test data"
    assert read_json_file("test.txt") == {}


@pytest.fixture()
def dict_with_transactions() -> dict:
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


def test_sum_amount(dict_with_transactions: dict) -> None:
    assert sum_amount(dict_with_transactions) == 31957.58


@patch("requests.get")
def test_convert_usd(mock_get: Any) -> None:
    mock_response = {"rates": {"RUB": 75.0}}
    mock_get.return_value.text = json.dumps(mock_response)
    transaction = {"amount": 100, "currency": "USD"}
    assert get_currency_rate(transaction) == 75.0


@patch("requests.get")
def test_convert_eur(mock_get: Any) -> None:
    mock_response = {"rates": {"RUB": 85.0}}
    mock_get.return_value.text = json.dumps(mock_response)
    transaction = {"amount": 100, "currency": "EUR"}
    assert get_currency_rate(transaction) == 85.0
