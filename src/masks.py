def mask_card(information: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    return information[:4] + " " + information[4:6] + "** **** " + information[-4:]


def mask_account(information: str) -> str:
    """Функция принимает на вход номер счёта и возвращает его маску."""
    return "**" + information[-4:]


def get_data(d: str) -> str:
    return
