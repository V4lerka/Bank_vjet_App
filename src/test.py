from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

test_data = [
    "Maestro 1596 8378 6870 5197",
    " Счет 64686473678894779589 ",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum8990922113665229",
    "VisaGold5999414228426353",
    "Счет73654108430135874305",
]

list_operations_test = [
    {"id": 41428829, "state": "EXECUTED", 'date': '2019-07-03T18:35:29.512364'},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

for item in test_data:
    result_bank_data = mask_account_card(item)
    print(result_bank_data)

print(get_date("2024-03-11T02:26:18.7698"))
print(filter_by_state(list_operations_test, "CANCELED"))
print(sort_by_date(list_operations_test, False))
