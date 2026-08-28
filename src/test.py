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

for item in test_data:
    result_bank_data = mask_account_card(item)
    print(result_bank_data)

print(get_date("2024-03-11T02:26:18.671407"))
