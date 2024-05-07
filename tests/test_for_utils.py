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


def test_read_json_file(path_to_json_file: str) -> None:
    assert len(read_json_file(path_to_json_file)) == 0


@pytest.fixture()
def dict_with_transactions() -> List[dict]:
    return [
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


def test_sum_amount(dict_with_transactions: List[dict]) -> None:
    assert sum_amount(dict_with_transactions) == 87941.37


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
