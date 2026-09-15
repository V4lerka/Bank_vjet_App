from src.masks import get_mask_card_number, get_mask_account
import pytest


def test_get_mask_card_number_wrong(wrong_numbers):
    assert get_mask_card_number(wrong_numbers) == "Номер карты должен содержать только цифры, к тому же без пробелов"


def test_get_mask_card_number_empty(empty_number):
    assert get_mask_card_number(empty_number) == "Вы ничего не ввели"


@pytest.mark.parametrize("card_number, expected", [("5456234556789012", "5456 23** **** 9012"),
                                                   (" 5456234556789012 ", "5456 23** **** 9012"),
                                                   ("234556789012",
                                                    "Номер карты должен содержать ровно 16 цифр, вы ввели 12"),
                                                   ("2", "Номер карты должен содержать ровно 16 цифр, вы ввели 1")
                                                   ])

def test_get_mask_card_number_rest_cases(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_account_wrong(wrong_numbers):
    assert get_mask_account(wrong_numbers) == "Номер счета должен содержать только цифры, к тому же без пробелов"


def test_get_mask_account_empty(empty_number):
    assert get_mask_account(empty_number) == "Вы ничего не ввели"
