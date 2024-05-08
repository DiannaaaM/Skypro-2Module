def mask_card(number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    if len(number) == 16:
        return number[:4] + " " + number[4:6] + "** **** " + number[-4:]
    return number


def mask_account(number: str) -> str:
    """Функция принимает на вход номер счёта и возвращает его маску."""
    if len(number) == 21:
        return "**" + number[-4:]
    return number
