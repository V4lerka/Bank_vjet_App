from src.processing import filter_by_state, sort_by_date
import pytest


@pytest.mark.parametrize("state, expected",
                         [("CANCELED",
                           [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 615064591, 'state': 'CANCELED',
                             'date': '2018-10-14T08:21:33.419441'}]),
                          ("EXECUTED",
                           [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])])
def test_filter_by_state(list_of_operations, state, expected):
    assert filter_by_state(list_of_operations, state) == expected


def test_filter_by_state_empty(list_of_operations_without_state):
    with pytest.raises(Exception) as e:
        filter_by_state(list_of_operations_without_state)
    assert str(e.value) == "Все операции не имеют статуса"


def test_filter_by_state_partly_empty(list_of_operations_partly_without_state):
    with pytest.raises(Exception) as e:
        filter_by_state(list_of_operations_partly_without_state)
    assert str(
        e.value) == "Операции в количестве 2 шт. не имеют статуса. Список операций со статусом: [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]"
