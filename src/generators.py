from typing import Any, Generator


def filter_by_currency(list_transactions: list[dict[str, Any]], currency: str) -> Generator[dict[str, Any]]:
    """Функция принимает на вход список словарей, представляющих транзакции, и возвращает итератор, который поочередно
    выдает транзакции, где валюта операции соответствует заданной"""
    for transaction in list_transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction

def transaction_descriptions(list_transactions: list[dict[str, Any]]) -> Generator[str]:
    """Принимает список словарей с транзакциями и возвращает итератор, который выдает описание каждой операции
    по очереди"""
    for transaction in list_transactions:
        yield transaction["description"]

