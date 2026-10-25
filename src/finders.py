from collections import Counter
import re


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Принимает список словарей с данными о банковских операциях и строку поиска, а возвращает список словарей,
    у которых в описании есть данная строка."""
    if data:
        pattern = fr"{search}"
        filtered_data = []
        for transaction in data:
            if transaction.get("description") is not None:
                if re.search(pattern, transaction["description"], flags=re.I):
                    filtered_data.append(transaction)
        if filtered_data:
            return filtered_data
        else:
            print("По вашему запросу ничего не найдено")
            return []
    else:
        print("Список транзакций пуст, анализ не возможен")
        return []


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Принимает список словарей с данными о банковских операциях и список категорий операций, а возвращает словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    if data:
        descriptions_from_data = [transaction["description"] for transaction in data if
                                  transaction.get("description") is not None]
        categories_from_data = []
        for category in categories:
            pattern = fr"{category}"
            for description in descriptions_from_data:
                if re.search(pattern, description, flags=re.I):
                    categories_from_data.append(category)
        result = {}
        if categories_from_data:
            counted_categories = Counter(categories_from_data)
            for category in categories:
                if category in counted_categories.keys():
                    result[category] = counted_categories[category]
                else:
                    result[category] = 0
            return result
        else:
            print("По вашему запросу ничего не найдено")
            for category in categories:
                result[category] = 0
            return result
    else:
        print("Список транзакций пуст, анализ не возможен")
        return {}
