import datetime
import logging
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                # Действие и запись в log_message сообщение, которое будет записывать в файл
                logging.info("Время выполнения: %s УСПЕШНО", datetime.datetime.now())
                log_message = f"Время выполнения: {datetime.datetime.now()} УСПЕШНО"
                result = func(*args, **kwargs)
            except Exception as e:
                # Действие если ошибка и запись в log_message сообщение, которуешь будет распечатано
                logging.error("Время выполнения: %s ОШИБКА: %s", datetime.datetime.now(), e)
                log_message = f"Время выполнения: {datetime.datetime.now()} ОШИБКА: {e}"
                result = func(*args, **kwargs)
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_message)
                file.close()
            else:
                print(log_message)
            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def return_date_and_operation(date: str, operation: str) -> str:
    """Возвращает строку с датой и операцией"""
    return f"Время операции: {date}. Операция: {operation}"


return_date_and_operation("2019-07-03T18:35:29.512364", 939719570)
