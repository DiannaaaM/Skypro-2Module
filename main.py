import time

from src.generators import filter_by_currency, random_card_number, returned_description
from src.libraries import count_categories, filter_by_state
from src.logger import setup_logging
from src.masks import mask_account, mask_card
from src.processing import sort_dicts_by_date, sorted_list_by_value
from src.reader_csv_xlsx_files import open_file
from src.utils import get_currency_rate, read_json_file, sum_amount
from src.widget import get_data, mask_account_and_card


def calling_functions(user_input, path_to_file, type_of_sort, currency=None, sort_of_date=None, filter_by_word=None):
    if user_input == "1":
        file = read_json_file(path_to_file)
    else:
        file = open_file(path_to_file)
    sort = sorted_list_by_value(file, type_of_sort.upper())
    if sort_of_date == "да":
        reverse_value = "asc" if sort_of_date == "по возрастанию" else "desc"
        sort = sort_dicts_by_date(sort, reverse_value)
    if currency == "да":
        for value in sort:
            value["amount"] = round(value["amount"] * get_currency_rate(), 2)
    if filter_by_word is not None:
        sort = filter_by_word(sort, filter_by_word)
    for value in sort:
        date = get_data(value["date"])
        description = value["description"]
        from_ = mask_account_and_card(value["from"])
        to = mask_account_and_card(value["to"])
        amount = value["operationAmount"]["amount"]
        return f"""{date} {description} \n{from_} -> {to} \nСумма: {amount}"""


print(
    """Привет! Добро пожаловать в программу работы с банковскими транзакициями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из json файла
2. Получить информацию о транзакциях из csv файла
3. Получить информацию о транзакциях из xlsx файла"""
)
user_input = input("выберите\t\t")
if user_input not in ["1", "2", "3"]:
    print("Но такого варианта нет... " "\nПопробуйте еще раз")
user_path_to_file = input("Введите путь до файла:\n")
type_of_sort = input(
    """Введите статус по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
)
verification_date = input("Отсортировать операции по дате? Да/Нет").lower()
if verification_date == "Да":
    sort_of_date = input("Отсортировать по:" "\n1. возрастанию" "\n.убыванию")
user_currency = input("Выводить только рублевые тразакции? Да/Нет")
Verification_filter_of_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
if Verification_filter_of_word == "Да":
    filter_by_word = input("Введите описание, по которому необходимо отсортировать\n").lower()
result = calling_functions(user_input, user_path_to_file, type_of_sort, sort_of_date, user_currency, filter_by_word)
print("Распечатываю итоговый список транзакций...")
time.sleep(1)
print(result)
