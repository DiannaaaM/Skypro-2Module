from unittest.mock import Mock, patch

import pytest

from src.utils import get_currency_rate, read_json_file, sum_amount


@pytest.fixture()
def dict_with_transactions():
    return {
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


def test_sum_amount(dict_with_transactions):
    assert sum_amount(dict_with_transactions) == 185795.22999999998
