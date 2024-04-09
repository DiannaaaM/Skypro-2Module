from datetime import datetime
from typing import List


def sorted_list_by_value(input_list: List[dict], state: str = "EXECUTED") -> List[dict]:
    """Функция, которая принимает на вход список словарей и значение для ключа
    и возвращает новый список, содержащий только те словари, у которых ключ содержит переданное в функцию значение."""
    return_list = []
    for value in input_list:
        if value["state"] == state:
            return_list.append(value)
    return return_list


def sort_dicts_by_date(input_list: List[dict], reverse: str = "desc") -> List[dict]:
    """Функция, которая принимает на вход список словарей
    и возвращает новый список, в котором исходные словари отсортированы по убыванию даты"""
    return sorted(
        input_list, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=(reverse == "desc")
    )
