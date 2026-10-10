import csv
import os
from typing import Any
import pandas as pd

def csv_reader(path: str) -> list[dict[str, Any]]:
    """Функция читает файлы csv с транзакциями и возвращает список словарей с транзакциями"""
    if path.endswith("csv"):
        full_path = os.path.join("../data", f"{path}")
        try:
            with open(full_path, encoding="utf-8") as transaction_file:
                data = csv.DictReader(transaction_file, delimiter=";")
                transactions_list = []
                for row in data:
                    transactions_list.append(row)
        except Exception as e:
            print(f"Возникла ошибка {e}")
            return []
    else:
        raise Exception("Формат файла не поддерживается")
    return transactions_list

print(csv_reader("trans.csv"))

def excel_reader(path: str) -> list[dict[str, Any]]:
    """Функция читает файлы excel с транзакциями и возвращает список словарей с транзакциями"""
    if path.endswith("xlsx") or path.endswith("xls"):
        full_path = os.path.join("../data", f"{path}")
        try:
            transactions_list = pd.read_excel(full_path).to_dict(orient="records")
        except Exception as e:
            print(f"Возникла ошибка {e}")
            return []
    else:
        raise Exception("Формат файла не поддерживается")
    return transactions_list

print(excel_reader("trans.xlsx"))