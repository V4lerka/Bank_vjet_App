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
                if type(data) != list:
                    print("Тип данных в файле не является списком")
                    return []
                return data
            except JSONDecodeError:
                print("Формат не соответствует JSON или файл пустой")
                return []
    except FileNotFoundError:
        print("Файл не найден по указанному пути")
        return []
