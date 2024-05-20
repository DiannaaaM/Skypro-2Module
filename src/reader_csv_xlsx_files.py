import csv
from typing import Any

import pandas as pd


def open_file(file_path: Any) -> str:
    with open(file_path, "r", encoding="latin1") as f:
        return f.read()


# print(open_file('../data/transactions.csv'))  # 147761
# print(open_file('../data/transactions_excel.xlsx'))  # 81998
