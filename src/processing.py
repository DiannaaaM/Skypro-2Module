from datetime import datetime
from typing import List
from typing import Any



def sorted_list_by_value(file: Any, state: str = "EXECUTED") -> List[dict]:
    """Функция, которая принимает на вход список словарей и значение для ключа
    и возвращает новый список, содержащий только те словари, у которых ключ содержит переданное в функцию значение."""
    result = []
    for value in file:
        if 'state' in value and value['state'] == state:
            result.append(value)
    return result


def sort_dicts_by_date(input_list: List[dict], reverse: str = "desc") -> List[dict]:
    """Функция, которая принимает на вход список словарей
    и возвращает новый список, в котором исходные словари отсортированы по убыванию даты"""
    return sorted(
        input_list, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=(reverse == "desc")
    )
