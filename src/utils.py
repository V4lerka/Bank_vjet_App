import json
import os
from json import JSONDecodeError
from typing import Any


def convert_json_to_list(path: str) -> list[dict[str, Any]]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""

    full_path = os.path.join("../data/", f"{path}")
    try:
        with open(full_path, encoding="utf-8") as file:
            try:
                data = json.load(file)
                if type(data) is not list:
                    print("Тип данных в файле не является списком")
                    return []
                return data
            except JSONDecodeError:
                print("Формат не соответствует JSON или файл пустой")
                return []
    except FileNotFoundError:
        print("Файл не найден по указанному пути")
        return []
