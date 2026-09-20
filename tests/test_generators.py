import pytest
from src.generators import filter_by_currency, transaction_descriptions
from tests.conftest import list_of_transactions


def test_filter_by_currency(list_of_transactions):
    generator = filter_by_currency(list_of_transactions, "RUB")
    assert next(generator) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
    }
    assert next(generator) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657"
    }

def test_filter_by_currency_empty():
    generator = filter_by_currency([], "RUB")
    assert next(generator) == {}


def test_filter_by_currency_is_absent(list_of_transactions):
    generator = filter_by_currency(list_of_transactions, "EUR")
    with pytest.raises(Exception) as e:
        next(generator)
    assert str(e.value) == "Операции с валютой EUR не обнаружены"


def test_transaction_descriptions(list_of_transactions):
    generator = transaction_descriptions(list_of_transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Описание транзакции с id 142264268 отсутствует"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"


def test_transaction_descriptions_empty():
    generator = transaction_descriptions([])
    assert next(generator) == "Транзакции не найдены"


