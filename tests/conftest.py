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
