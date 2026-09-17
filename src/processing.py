from typing import Any
import re


def filter_by_state(list_operations: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция принимает список словарей и опционально значение для ключа state (по умолчанию
    'EXECUTED') и возвращает новый список тех словарей, у которых ключ state соответствует указанному"""
    filtered_operations = []
    operations_without_state = []
    for operation in list_operations:
        if operation.get("state") == state:
            filtered_operations.append(operation)
        elif operation.get("state") is None:
            operations_without_state.append(operation)
    if len(filtered_operations) == 0:
        raise Exception(f"Все операции не имеют статуса")
    if len(operations_without_state) > 0:
        raise Exception(
            f"Операции в количестве {len(operations_without_state)} шт. не имеют статуса. Список операций со статусом: {filtered_operations}")
    return filtered_operations


def sort_by_date(list_operations: list[dict[str, Any]], descending_order: bool = True) -> list[dict[str, Any]]:
    """Функция принимает список словарей и параметр, задающий порядок сортировки (по умолчанию — убывание)
    и возвращает новый список, отсортированный по дате (date)"""
    sorted_operations: list[dict[str, Any]] = []
    new_list_operations: list[dict[str, Any]] = []
    new_list_operations_without_date: list[dict[str, Any]] = []
    for operation in list_operations:
        if operation.get("date") is not None:
            parse_iso_data = re.findall(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", operation.get("date"))
            if parse_iso_data:
                new_list_operations.append(operation)
        elif operation.get("date") is None:
            new_list_operations_without_date.append(operation)
    if len(new_list_operations) == 0:
        return sorted_operations
    elif descending_order and len(new_list_operations) == len(list_operations):
        sorted_operations = sorted(new_list_operations, key=lambda operations: operations["date"], reverse=True)
    elif not descending_order and len(new_list_operations) == len(list_operations):
        sorted_operations = sorted(new_list_operations, key=lambda operations: operations["date"])
    elif descending_order and len(new_list_operations) < len(list_operations):
        sorted_operations = sorted(new_list_operations, key=lambda operations: operations["date"], reverse=True)
        updated_sorted_operations = sorted_operations + new_list_operations_without_date
        return updated_sorted_operations
    elif not descending_order and len(new_list_operations) < len(list_operations):
        sorted_operations = sorted(new_list_operations, key=lambda operations: operations["date"])
        updated_sorted_operations = sorted_operations + new_list_operations_without_date
        return updated_sorted_operations
    return sorted_operations
