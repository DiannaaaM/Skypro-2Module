import random
from typing import Generator, Iterator, List


def filter_by_currency(transactions: List[dict], currency: str = "USD") -> Iterator[dict]:
    """
    Функция, которая принимает список словарей,
    и возвращает итератор, который выдает по очереди операции, в которых указана заданная валюта.
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction["id"]


def returned_description(transactions: List[dict]) -> Generator[str, None, None]:
    """
    Генератор, который принимает список словарей и возвращает описание каждой операции по очереди.
    """
    for transaction in transactions:
        yield str(transaction.get("description"))


def random_card_number(start: int, stop: int) -> Generator[str, None, None]:
    """
    Генератор номеров банковских карт, который должен генерировать номера карт
    в формате "XXXX XXXX XXXX XXXX", где X — цифра.
    Должны быть сгенерированы номера карт в заданном диапазоне
    """
    while True:
        card_number = "".join([str(random.randint(start, stop)) for _ in range(16)])
        yield " ".join(card_number[i : i + 4] for i in range(0, len(card_number), 4))
