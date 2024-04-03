def new_mask_card(information: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    if "Visa" in information or "MasterCard" in information:
        words = information.split()
        masked_str = ""
        for word in words:
            if word.isdigit() and len(word) == 16:
                masked_word = word[:2] + "** **** " + word[-4:]
                masked_str += masked_word + " "
            else:
                masked_str += word + " "
        return masked_str.strip()
    else:
        return information


def new_mask_account(information: str) -> str:
    """Функция принимает на вход номер счёта и возвращает его маску."""
    if "Счет" in information:
        words = information.split()
        masked_str = ""
        for word in words:
            if word.isdigit() and len(word) >= 16:
                maskedword = "**" + word[-4:]
                masked_str += maskedword + " "
            else:
                masked_str += word + " "
        return masked_str.strip()
    else:
        return information


def get_data(d: str) -> str:
    """ Функция, которая принимает на вход строку и возвращает строку с датой"""
    return f'{d[8:10]}.{d[5:7]}.{d[0:4]}'
