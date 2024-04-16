# from src.masks import mask_account, mask_card
# from src.widget import get_data, mask_account_and_card
from src.processing import sort_dicts_by_date, sorted_list_by_value

# user_input = input("Номер карты:")
# print(mask_account(user_input))
# user_inp = input("Номер счета:")
# print(mask_card(user_inp))
#
# user_input_card_or_account = input("Информация типа карты/счета и номер карты/счета")
# print(mask_account_and_card(user_input_card_or_account))
# user_input_data = input('Дата(вида "2018-07-11T02:26:18.671407"): ')
# print(get_data(user_input_data))

print(
    sorted_list_by_value(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        "CANCELED",
    )
)
print(
    sort_dicts_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        reverse="desc",
    )
)
