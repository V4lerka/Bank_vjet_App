import csv
import os
from typing import Any

import pandas as pd


def csv_reader(path: str) -> list[dict[str, Any]]:
    """Функция читает файлы csv с транзакциями и возвращает список словарей с транзакциями"""
    if path.lower().endswith("csv"):
        full_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data", f"{path}"))
        transactions_list = []
        try:
            with open(full_path, encoding="utf-8") as transaction_file:
                data = csv.DictReader(transaction_file, delimiter=";")
                transactions_list = list(data)
        except FileNotFoundError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Возникла непредвиденная ошибка: {e}")
    else:
        raise Exception("Формат файла не поддерживается")
    return transactions_list


def excel_reader(path: str) -> list[dict[str, Any]]:
    """Функция читает файлы excel с транзакциями и возвращает список словарей с транзакциями"""
    if path.lower().endswith("xlsx") or path.lower().endswith("xls"):
        full_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data", f"{path}"))
        transactions_list = []
        try:
            transactions_list = pd.read_excel(full_path).to_dict(orient="records")
        except FileNotFoundError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Возникла непредвиденная ошибка: {e}")
    else:
        raise Exception("Формат файла не поддерживается")
    return transactions_list
