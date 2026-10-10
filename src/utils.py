import json
import logging
import os
from json import JSONDecodeError
from typing import Any

log_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../logs/", "app.log"))
utils_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"{log_path}", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)
utils_logger.setLevel(logging.DEBUG)


def convert_json_to_list(path: str) -> list[dict[str, Any]]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""

    full_path = os.path.join("../data/", f"{path}")
    utils_logger.info(f"Попытка открытия файла {path}")
    try:
        with open(full_path, encoding="utf-8") as file:
            utils_logger.info(f"Попытка чтения файла {path}")
            try:
                data = json.load(file)
                if type(data) is not list:
                    utils_logger.error("Тип данных не соответствует. Возвращен пустой список")
                    print("Тип данных в файле не является списком")
                    return []
                utils_logger.info("Функция успешно завершила работу")
                return data
            except JSONDecodeError as e:
                utils_logger.error(f"Произошла ошибка {e}")
                print("Формат не соответствует JSON или файл пустой")
                return []
    except FileNotFoundError as e:
        utils_logger.error(f"Произошла ошибка {e}")
        print("Файл не найден по указанному пути.")
        return []
