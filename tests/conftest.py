import pytest


@pytest.fixture(params=["q1223g0003443443f", "card_number123456789677", "#66734998478998379858 ", " №90849040953274893",
                        "1O45090948O8355757", "4843 9034 3456 2311", "visa 1234098765431234"])
def wrong_numbers(request):
    return request.param


@pytest.fixture(params=["", "      "])
def empty_number(request):
    return request.param


@pytest.fixture(params=[1245567687687, [324647654787438], (3423, 4567, 7699, 6565)])
def wrong_type(request):
    return request.param


@pytest.fixture(params=["124", "  284", " 26 ", "1"])
def short_len(request):
    return request.param


@pytest.fixture
def big_len():
    return "576897535467458997897886"


@pytest.fixture(params=["visa gold 4688", "счет123#", "visa ", "Счет №   ", "Mastercard 456?343;343!1230",
                        "Сч. 1234 5445", "Visa Gold 468823454549045678912345", "   ", 12345556
                        ])
def invalid_bank_data(request):
    return request.param


@pytest.fixture
def list_of_operations():
    return [{"id": 41428829, "state": "EXECUTED", 'date': '2019-07-03T18:35:29.512364'},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]

@pytest.fixture
def list_of_operations_without_state():
    return [{"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
            ]

@pytest.fixture
def list_of_operations_partly_without_state():
    return [{'id': 41428829, 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            ]

@pytest.fixture
def list_of_operations_without_date():
    return [{"id": 41428829, "state": "EXECUTED"},
            {"id": 939719570, "state": "EXECUTED"},
            {"id": 594226727, "state": "CANCELED"},
            {"id": 615064591, "state": "CANCELED"},
            ]

@pytest.fixture
def list_of_operations_partly_without_date():
    return [{'id': 41428829, 'state': 'EXECUTED'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            ]


@pytest.fixture
def list_of_operations_not_iso_date():
    return [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]