from src.external_api import show_transactions_amount
from src.finders import process_bank_search
from src.generators import filter_by_currency, transaction_descriptions
from src.processing import filter_by_state, sort_by_date
from src.readers import csv_reader, excel_reader
from src.utils import convert_json_to_list
from src.widget import get_date, mask_account_card


def main():
    """Основная функция, которая связывает все функциональности из модулей, формируя общую логику программы"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        user_input = input("""Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла\n""")
        if user_input.strip() == "1":
            print("Для обработки выбран JSON-файл.")
            data = convert_json_to_list("operations.json")
            break
        elif user_input.strip() == "2":
            print("Для обработки выбран CSV-файл.")
            data = csv_reader("transactions.csv")
            for transaction in data:
                transaction["operationAmount"] = {
                    "amount": transaction.get("amount"),
                    "currency": {"name": transaction.get("currency_name"), "code": transaction.get("currency_code")},
                }
                transaction.pop("amount")
                transaction.pop("currency_name")
                transaction.pop("currency_code")
                value = transaction.get("from")
                if value != value or value is None or str(value) == "":
                    transaction.pop("from")
            break
        elif user_input.strip() == "3":
            print("Для обработки выбран XLSX-файл.")
            data = excel_reader("transactions_excel.xlsx")
            for transaction in data:
                transaction["operationAmount"] = {
                    "amount": transaction.get("amount"),
                    "currency": {"name": transaction.get("currency_name"), "code": transaction.get("currency_code")},
                }
                transaction.pop("amount")
                transaction.pop("currency_name")
                transaction.pop("currency_code")
                value = transaction.get("from")
                if value != value or value is None or str(value) == "":
                    transaction.pop("from")
            break
        else:
            print("ОШИБКА!\nУказанный пункт меню не существует. Повторите попытку.")

    while True:
        user_input_status = input("""Введите статус, по которому необходимо выполнить фильтрацию операций.
Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING\n""")
        if user_input_status.upper().strip() == "EXECUTED":
            filtered_data = filter_by_state(data)
            print("Операции отфильтрованы по статусу 'EXECUTED'")
            break
        elif user_input_status.upper().strip() == "CANCELED":
            filtered_data = filter_by_state(data, "CANCELED")
            print("Операции отфильтрованы по статусу 'CANCELED'")
            break
        elif user_input_status.upper().strip() == "PENDING":
            filtered_data = filter_by_state(data, "PENDING")
            print("Операции отфильтрованы по статусу 'PENDING'")
            break
        else:
            print(f"ОШИБКА!\nСтатус операции '{user_input_status}' недоступен. Повторите попытку.")

    while True:
        user_input_add1 = input("Отсортировать операции по дате? Да/Нет\n")
        if user_input_add1.lower().strip() == "да":
            while True:
                user_input_add2 = input("Отсортировать по возрастанию или по убыванию? По возрастанию / по убыванию\n")
                if user_input_add2.lower().strip() == "по убыванию":
                    sorted_data_with_order = sort_by_date(filtered_data)
                    break
                elif user_input_add2.lower().strip() == "по возрастанию":
                    sorted_data_with_order = sort_by_date(filtered_data, False)
                    break
                else:
                    print("ОШИБКА! Некорректный ввод. Повторите ввод.")
            break
        elif user_input_add1.lower().strip() == "нет":
            sorted_data_with_order = filtered_data
            break
        else:
            print("ОШИБКА! Некорректный ввод. Повторите ввод.")
    switcher = 0
    while True:
        user_input_add3 = input("Выводить только рублевые транзакции? Да/Нет\n")
        if user_input_add3.lower().strip() == "да":
            target_curr_transactions = list(filter_by_currency(sorted_data_with_order, "RUB"))
            switcher += 0
            break
        elif user_input_add3.lower().strip() == "нет":
            while True:
                user_input_convert = input(
                    "Выполнить конвертацию иностранной валюты в рубли по текущему курсу? Да/Нет\n"
                )
                if user_input_convert.lower().strip() == "нет":
                    target_curr_transactions = sorted_data_with_order
                    switcher += 0
                    break
                elif user_input_convert.lower().strip() == "да":
                    target_curr_transactions = sorted_data_with_order
                    switcher += 1
                    break
                else:
                    print("ОШИБКА! Некорректный ввод. Повторите ввод.")
            break
        else:
            print("ОШИБКА! Некорректный ввод. Повторите ввод.")

    while True:
        user_input_add4 = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
        if user_input_add4.lower().strip() == "да":
            user_input_add5 = input("Введите ключевое слово для поиска:\n")
            filtered_by_user = process_bank_search(target_curr_transactions, user_input_add5)
            break
        elif user_input_add4.lower().strip() == "нет":
            filtered_by_user = target_curr_transactions
            break
        else:
            print("ОШИБКА! Некорректный ввод. Повторите ввод.")

    if filtered_by_user:
        print("Распечатываю итоговый список транзакций...\n")
        print(f"Всего банковских операций в выборке: {len(filtered_by_user)}\n")
        gen_descriptions = transaction_descriptions(filtered_by_user)
        for transaction in filtered_by_user:
            print(f"{get_date(transaction.get("date"))} {next(gen_descriptions)}")
            if transaction.get("from") is not None:
                print(f"{mask_account_card(transaction.get("from"))} -> {mask_account_card(transaction.get("to"))}")
            else:
                print(f"{mask_account_card(transaction.get("to"))}")
            if switcher == 0:
                print(
                    f"Сумма: {transaction.get("operationAmount").get("amount")} "
                    f"{transaction.get("operationAmount").get("currency").get("code")}\n"
                )
            elif switcher == 1:
                print(f"Сумма: {show_transactions_amount(transaction)} руб.\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()
