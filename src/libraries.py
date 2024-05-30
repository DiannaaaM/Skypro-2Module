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


def count_categories(transactions: list) -> Dict[str, int]:
    """Функция, которая принимает на вход список словарей и возвращает словарь,
    в котором ключами являются категории операций, а значениями - количество операций в каждой категории."""
    states_count: Dict[str, int] = Counter()
    for transaction in transactions:
        state = transaction.get("state")
        if state is not None:
            states_count.update([state])

    return states_count


# transactions = [
#     {
#         "id": 441945886,
#         "state": "CANCELED",
#         "date": "2019-08-26T10:50:58.294041",
#         "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
#         "description": "Перевод организации",
#         "from": "Maestro 1596837868705199",
#         "to": "Счет 64686473678894779589",
#     },
#     {
#         "id": 41428829,
#         "state": "EXECUTED",
#         "date": "2019-07-03T18:35:29.512364",
#         "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод организации",
#         "from": "MasterCard 7158300734726758",
#         "to": "Счет 35383033474447895560",
#     },
# ]

# result = count_categories(read_json_file("../data/operations.json"))
# print(result)

res = filter_by_state((read_json_file("../data/operations.json")), "Перевод организации")
print(res)
