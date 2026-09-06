from typing import Any


def filter_by_state(list_operations: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция принимает список словарей и опционально значение для ключа state (по умолчанию
    'EXECUTED') и возвращает новый список тех словарей, у которых ключ state соответствует указанному"""
    filtered_operations = []
    for operation in list_operations:
        if operation.get("state") == state:
            filtered_operations.append(operation)
    return filtered_operations


def sort_by_date(list_operations: list[dict[str, Any]], descending_order: bool = True) -> list[dict[str, Any]]:
    """Функция принимает список словарей и параметр, задающий порядок сортировки (по умолчанию — убывание)
    и возвращает новый список, отсортированный по дате (date)"""
    sorted_operations: list[dict[str, Any]] = []
    new_list_operations: list[dict[str, Any]] = []
    for operation in list_operations:
        if operation.get("date") is not None:
            new_list_operations.append(operation)
    if len(new_list_operations) == 0:
        return sorted_operations
    elif descending_order:
        sorted_operations = sorted(new_list_operations, key=lambda operations: operations["date"], reverse=True)
    elif not descending_order:
        sorted_operations = sorted(new_list_operations, key=lambda operations: operations["date"])
    return sorted_operations
