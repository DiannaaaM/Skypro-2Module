import unittest
from unittest.mock import patch

from src.utils import get_currency_rate


class TestTransactionAmount(unittest.TestCase):

    @patch("utils.requests.get")
    def test_convert_usd(self, mock_get: str) -> None:
        mock_response = {"rates": {"RUB": 75.0}}
        mock_get.return_value.json.return_value = mock_response
        transaction = {"amount": 100, "currency": "USD"}
        self.assertEqual(get_currency_rate(transaction), 7500)

    @patch("utils.requests.get")
    def test_convert_eur(self, mock_get: str) -> None:
        mock_response = {"rates": {"RUB": 85.0}}
        mock_get.return_value.json.return_value = mock_response
        transaction = {"amount": 100, "currency": "EUR"}
        self.assertEqual(get_currency_rate(transaction), 8500)
