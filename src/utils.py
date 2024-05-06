import json
import os
from typing import Any


def read_json_file(file_name: str) -> Any:
    """
    Читает json файл и возвращает данные в виде словаря
    """
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return {}


file = os.path.abspath(os.path.join("..", "data", "operations.json"))
print(read_json_file(file))
