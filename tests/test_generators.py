import pytest
from src.generators import filter_by_currency, transaction_descriptions
from tests.conftest import list_of_transactions


def test_filter_by_currency(list_of_transactions):
    generator = filter_by_currency(list_of_transactions, "RUB")
    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "RUB",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    }
    assert next(generator) == {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-05-04T23:20:05.206878",
            "operationAmount": {
                "amount": "9114.93",
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 29708645243227258542",
            "to": "Счет 85651667383060284188"
        }

def test_transaction_descriptions(list_of_transactions):
    generator = transaction_descriptions(list_of_transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета карты на счет вклада"

