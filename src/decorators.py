import datetime
from functools import wraps
from typing import Any, Callable

logfile = open("mylog.txt", "a", encoding="utf-8")


def log(func: Callable) -> Callable:
    """Генератор, который записывает дату и операцию в файл"""

    @wraps(func)
    def inner(*args: Any,
          **kwargs: Any) -> Any:
        logfile.write(f"Дата: {datetime.datetime.now()}  УСПЕШНО\n")
        return func(*args, *kwargs)

    return inner


@log
def return_date_and_operation(date: str, operation: str) -> str:
    """Возвращает строку с датой и операцией"""
    return f"Время операции: {date}. Операция: {operation}"


return_date_and_operation("2019-07-03T18:35:29.512364", 939719570)
