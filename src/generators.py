from typing import Generator, Any


def filter_by_currency(list_transactions: list[dict[str, Any]], currency: str) -> Generator[
    dict[str, Any]]:
    """Функция принимает на вход список словарей, представляющих транзакции, и возвращает итератор, который поочередно
    выдает транзакции, где валюта операции соответствует заданной"""
    if len(list_transactions) == 0:
        yield {}
    elif len(list_transactions) > 0:
        currency_list = [
            transaction.get("operationAmount").get("currency").get("code")
            for transaction in list_transactions
            if transaction.get("operationAmount").get("currency") is not None
        ]
        if currency not in currency_list:
            raise Exception(f"Операции с валютой {currency} не обнаружены")
        for transaction in list_transactions:
            if transaction.get("operationAmount").get("currency") is None:
                continue
            elif transaction.get("operationAmount").get("currency").get("code") == currency:
                yield transaction


def transaction_descriptions(list_transactions: list[dict[str, Any]]) -> Generator[str]:
    """Принимает список словарей с транзакциями и возвращает итератор, который выдает описание каждой операции
    по очереди"""
    if len(list_transactions) == 0:
        yield "Транзакции не найдены"
    for transaction in list_transactions:
        if transaction.get("description") is not None:
            yield transaction["description"]
        else:
            yield f"Описание транзакции с id {transaction.get("id", "Неизвестен")} отсутствует"


def card_number_generator(start: int, stop: int) -> Generator[str]:
    """Функция-генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX при заданном
    диапазоне генерации"""
    for i in range(start, stop + 1):
        num_str = str(i)
        card_number = "0" * (16 - len(num_str)) + num_str
        four_groups = [card_number[4 * n: 4 * (n + 1)] for n in range(4)]
        yield " ".join(four_groups)
