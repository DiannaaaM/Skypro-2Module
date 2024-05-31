import re
from collections import Counter
from typing import Any, Dict

from src.utils import read_json_file


def filter_by_state(transactions: list, search: str) -> list:
    """Функция, которая принимает на вход список словарей и значение для ключа
    и возвращает новый список, содержащий только те словари, у которых ключ содержит переданное в функцию значение."""
    result = []
    for transaction in transactions:
        if "description" in transaction and re.search(search, transaction["description"]):
            result.append(transaction)
    return result


def count_categories(transactions: list, categories: dict) -> Dict[str, int]:
    """Функция, которая принимает на вход список словарей и возвращает словарь,
    в котором ключами являются категории операций, а значениями - количество операций в каждой категории."""
    categories_count: Dict[str, int] = {category: 0 for category in categories.values()}
    for transaction in transactions:
        for key, value in transaction.items():
            for category_key, category_value in categories.items():
                if value == category_value and value is not None:
                    categories_count[category_value] += 1
    return categories_count


# result = count_categories(read_json_file("../data/operations.json"), {'category_1': "Перевод", 'category_2': "EXECUTED"})
# print(result)

# res = filter_by_state((read_json_file("../data/operations.json")), "Перевод организации")
# print(res)
