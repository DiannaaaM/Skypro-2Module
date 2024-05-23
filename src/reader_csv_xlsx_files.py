import csv
from typing import Any

import pandas as pd


def open_file(file_path: Any) -> Any:
    transcriptions = []
    if file_path.endswith(".csv"):
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=";")
            for row in reader:
                transcriptions.append(
                    {
                        "id": row[0],
                        "state": row[1],
                        "date": row[2],
                        "amount": row[3],
                        "currency_name": row[4],
                        "currency_code": row[5],
                        "from": row[6],
                        "to": row[7],
                        "description": row[8],
                    }
                )
                # Добавляем строку в список
        transcriptions.pop(0)
        return transcriptions
    elif file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path)
        return df.to_dict(orient="records")
    else:
        return "Неверный формат файла"


# print(open_file('../data/transactions.csv'))
# print(open_file('../data/transactions_excel.xlsx'))
