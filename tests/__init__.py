from src.masks import mask_account, mask_card
from scr.widget import new_mask_card, new_mask_account, get_data

user_input = input()
if len(user_input) == 20:
    print(mask_account(user_input))
else:
    print(mask_card(user_input))

user_input_card = input("номер карты: ")
user_input_bill = input("номер счета: ")
user_input_data = input('Дата(вида "2018-07-11T02:26:18.671407"): ')
print(new_mask_card(user_input_card))
print(new_mask_account(new_mask_account))
print(get_data(user_input_data))
