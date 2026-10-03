import json
from json import JSONDecodeError
from typing import Any
import os

def convert_json_to_list(path: str) -> list[dict[str, Any]]:
    """функция принимает на вход путь до JSON - файла и возвращает список словарей с данными о финансовых транзакциях"""

    full_path = os.path.join("../data/", f"{path}")
    try:
        with open(full_path, encoding="utf-8") as file:
            try:
                data = json.load(file)
            except JSONDecodeError:
                print("Ошибка декодирования: Файл пуст или имеет неверный формат")
                return []
            else:
                return data
    except FileNotFoundError:
        print("Файл не найден по указаному пути")
        return []


print(convert_json_to_list("operations.json"))
