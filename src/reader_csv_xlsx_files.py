import csv
from typing import Any

import pandas as pd


def open_file(file_path: Any) -> str:
    if file_path.endswith(".csv"):
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)
    elif file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path)
        return df.head()
    else:
        with open(file_path, "r", encoding="latin1") as f:
            return f.read()


# print(open_file('../data/transactions.csv'))  # 147761
# print(open_file('../data/transactions_excel.xlsx'))  # 81998
