import random
from typing import Generator, Iterator, List


def filter_by_currency(transactions: List[dict[str, int]], currency: str = "USD") -> Iterator[dict[str, int]]:
    """
    Функция, которая принимает список словарей,
    и возвращает итератор, который выдает по очереди операции, в которых указана заданная валюта.
    """
    for transaction in transactions:
        if transaction.get("currency") == currency:
            yield transaction


def returned_description(transactions: List[dict]) -> Generator[str, None, None]:
    """
    Генератор, который принимает список словарей и возвращает описание каждой операции по очереди.
    """
    for transaction in transactions:
        yield str(transaction.get("description"))


def random_card_number(start: int, stop: int) -> Generator[int, None, None]:
    """
    Генератор номеров банковских карт, который должен генерировать номера карт
    в формате "XXXX XXXX XXXX XXXX", где X — цифра.
    Должны быть сгенерированы номера карт в заданном диапазоне
    """
    while True:
        yield random.randint(start, stop)