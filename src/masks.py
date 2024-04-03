def mask_card(number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    return number[:4] + " " + number[4:6] + "** **** " + number[-4:]


def mask_account(number: str) -> str:
    """Функция принимает на вход номер счёта и возвращает его маску."""
    return "**" + number[-4:]