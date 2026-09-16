from src.widget import get_date, mask_account_card
import pytest


@pytest.mark.parametrize("bank_user_data, expected", [("Maestro 1596 8378 6870 5197", "Maestro 1596 83** **** 5197"),
                                                      (" Счет 64686473678894779589 ", "Счет **9589"),
                                                      ("MasterCard 7158300734726758",
                                                       "Master Card 7158 30** **** 6758"),
                                                      ("Счет 35383033474447895560", "Счет **5560"),
                                                      ("Visa Classic 6831982476737658",
                                                       "Visa Classic 6831 98** **** 7658"),
                                                      ("Visa Platinum8990922113665229",
                                                       "Visa Platinum 8990 92** **** 5229"),
                                                      ("VisaGold5999414228426353", "Visa Gold 5999 41** **** 6353"),
                                                      ("Счет73654108430135874305", "Счет **4305"),
                                                      ("счет №10000843013","Счет **3013"),
                                                      ("счет № 1000 08430 1378", "Счет **1378"),
                                                      ("счет 5678", "Счет 5678"),
                                                      ("Счет 56987", "Счет *6987")
                                                      ])
def test_mask_account_card_success(bank_user_data, expected):
    assert mask_account_card(bank_user_data) == expected


def test_mask_account_card_bad_case(invalid_bank_data):
    with pytest.raises(Exception):
        mask_account_card(invalid_bank_data)
