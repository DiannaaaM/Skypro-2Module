from src.masks import mask_account, mask_card

user_input = input()
if len(user_input) == 20:
    print(mask_account(user_input))
else:
    print(mask_card(user_input))
