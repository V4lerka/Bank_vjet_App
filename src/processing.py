from typing import Any

def filter_by_state(list_operations: list[dict[str, Any]], state: str = "EXECUTED") -> dict[str, Any]:
    """Функция принимает список словарей и опционально значение для ключа state (по умолчанию
'EXECUTED') и возвращает новый список тех словарей, у которых ключ state соответствует указанному"""
    pass

def sort_by_date(list_operations: list[dict[str, Any]], sort_order: bool = True) -> dict[str, Any]:
    """Функция принимает список словарей и параметр, задающий порядок сортировки (по умолчанию — убывание)
и возвращает новый список, отсортированный по дате (date)"""
    pass