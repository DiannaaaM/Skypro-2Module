from src.masks import mask_account, mask_card
from src.widget import get_data, mask_account_and_card

user_input = input("Номер карты:")
print(mask_account(user_input))
user_inp = input("Номер счета:")
print(mask_card(user_inp))
user_input_card_or_account = input("Информация типа карты/счета и номер карты/счета")
print(mask_account_and_card(user_input_card_or_account))
user_input_data = input('Дата(вида "2018-07-11T02:26:18.671407"): ')
print(get_data(user_input_data))
