from typing import Any
from unittest.mock import Mock, patch

from src.reader_csv_xlsx_files import open_file


def test_read_csv() -> None:
    assert len(open_file("../data/transactions.csv")) == 147761


@patch("builtins.open", create=True)
def test_read_xlsx(mock_open: Any) -> None:
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = "test data base"
    assert len(open_file("../data/transactions_excel.xlsx")) == 14
