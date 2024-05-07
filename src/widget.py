from src.masks import mask_account, mask_card


def mask_account_and_card(information: str) -> str:
    """Умеет работать как с картами, так и с счетами.
    Принимает на вход строку информацией тип карты/счета и номер карты/счета и
    возвращает эту строку с замаскированным номером карты/счета"""
    if "Счет" in information:
        words = information.split()
        masked_str = ""
        for word in words:
            if word.isdigit() and len(word) >= 16:
                masked_str += mask_account(word) + " "
            else:
                masked_str += word + " "
        return masked_str.strip()
    if "Visa" in information or "MasterCard" in information or "Maestro" in information:
        words = information.split()
        masked_str = ""
        for word in words:
            if word.isdigit() and len(word) >= 16:
                masked_str += mask_card(word) + " "
            else:
                masked_str += word + " "
        return masked_str
    else:
        return information


def get_data(d: str) -> str:
    """Функция, которая принимает на вход строку и возвращает строку с датой"""
    return f"{d[8:10]}.{d[5:7]}.{d[0:4]}"
