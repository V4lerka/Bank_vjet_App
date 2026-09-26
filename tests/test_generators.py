import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

@pytest.mark.parametrize("currency, expected", [
    ("RUB", [{
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
    },
        {
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
    ]),

    ("USD", [{
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }, {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        }

    ])

])
def test_filter_by_currency(list_of_transactions, currency, expected):
    generator = list(filter_by_currency(list_of_transactions, currency))
    assert generator == expected


def test_filter_by_currency_empty():
    generator = filter_by_currency([], "RUB")
    assert next(generator) == {}


def test_filter_by_currency_is_absent(list_of_transactions):
    generator = filter_by_currency(list_of_transactions, "EUR")
    with pytest.raises(Exception) as e:
        next(generator)
    assert str(e.value) == "Операции с валютой EUR не обнаружены"


@pytest.mark.parametrize("expected", [
                            (["Перевод организации",
                            "Описание транзакции с id 142264268 отсутствует",
                            "Перевод со счета на счет",
                            "Перевод с карты на карту",
                            "Перевод организации"]),
])
def test_transaction_descriptions(list_of_transactions, expected):
    generator = list(transaction_descriptions(list_of_transactions))
    assert generator == expected


def test_transaction_descriptions_empty():
    generator = transaction_descriptions([])
    assert next(generator) == "Транзакции не найдены"


@pytest.mark.parametrize("start, stop, expected", [
    (1, 5, ["0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003",
            "0000 0000 0000 0004",
            "0000 0000 0000 0005"]),
])
def test_card_number_generator1(start, stop, expected):
    generator = list(card_number_generator(start, stop))
    assert generator == expected


@pytest.mark.parametrize("start, stop, expected", [
    (2344_5999_9989_9990, 2344_5999_9989_9999,
     ["2344 5999 9989 9990", "2344 5999 9989 9991", "2344 5999 9989 9992",
      "2344 5999 9989 9993", "2344 5999 9989 9994", "2344 5999 9989 9995",
      "2344 5999 9989 9996", "2344 5999 9989 9997", "2344 5999 9989 9998", "2344 5999 9989 9999"]),
])
def test_card_number_generator2(start, stop, expected):
    generator = list(card_number_generator(start, stop))
    assert generator == expected
