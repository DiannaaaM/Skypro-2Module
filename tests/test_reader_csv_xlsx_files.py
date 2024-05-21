from typing import Any
from unittest.mock import MagicMock, Mock, patch

import pandas as pd

from src.reader_csv_xlsx_files import open_file


def test_read_csv() -> None:
    assert len(open_file("../data/transactions.csv")) == 1000


@patch("pandas.read_excel", create=True)
def test_read_xlsx(mock_open: Any) -> None:
    mock_file = mock_open()
    mock_file.enter().read.return_value = pd.DataFrame({
        "id": ["1", "2"],
        "first_name": ["John", "Jane"],
        "last_name": ["Doe", "Smith"]
    })
    assert open_file("test.xlsx").equals(pd.DataFrame({
        "id": ["1", "2"],
        "first_name": ["John", "Jane"],
        "last_name": ["Doe", "Smith"]
    }))