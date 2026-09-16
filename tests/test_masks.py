from src.masks import get_mask_card_number, get_mask_account
import pytest


def test_get_mask_card_number_wrong(wrong_numbers):
    with pytest.raises(Exception) as e:
        get_mask_card_number(wrong_numbers)
    assert str(e.value) == "Номер карты должен содержать только цифры без пробелов"


def test_get_mask_card_number_empty(empty_number):
    with pytest.raises(Exception) as e:
        get_mask_card_number(empty_number)
    assert str(e.value) == "Вы ничего не ввели"


def test_get_mask_card_number_type(wrong_type):
    with pytest.raises(TypeError) as e:
        get_mask_card_number(wrong_type)
    assert str(e.value) == "Неверный тип введенных данных"


@pytest.mark.parametrize("card_number, expected", [("5456234556789012", "5456 23** **** 9012"),
                                                   (" 5456234556789012 ", "5456 23** **** 9012"),
                                                   ])
def test_get_mask_card_number_success(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_short_len(short_len):
    with pytest.raises(Exception) as e:
        get_mask_card_number(short_len)
    assert str(e.value) == "Номер карты должен содержать ровно 16 цифр, вы ввели меньше"


def test_get_mask_card_number_big_len(big_len):
    with pytest.raises(Exception) as e:
        get_mask_card_number(big_len)
    assert str(e.value) == "Номер карты должен содержать ровно 16 цифр, вы ввели больше"


def test_get_mask_account_wrong(wrong_numbers):
    with pytest.raises(Exception) as e:
        get_mask_account(wrong_numbers)
    assert str(e.value) == "Номер счета должен содержать только цифры без пробелов"


def test_get_mask_account_empty(empty_number):
    with pytest.raises(Exception) as e:
        get_mask_account(empty_number)
    assert str(e.value) == "Вы ничего не ввели"


def test_get_mask_account_type(wrong_type):
    with pytest.raises(TypeError) as e:
        get_mask_account(wrong_type)
    assert str(e.value) == "Неверный тип введенных данных"


def test_get_mask_account_short(short_len):
    with pytest.raises(Exception) as e:
        get_mask_account(short_len)
    assert str(e.value) == "Номер счета слишком короткий. Минимальная длина 4 цифры"


@pytest.mark.parametrize("account_number, expected", [("5456", "5456"),
                                                   ("54562", "*4562"),
                                                    ("545624", "**5624"),
                                                    ("545005624", "**5624")
                                                   ])
def test_get_mask_account_success(account_number, expected):
    assert get_mask_account(account_number) == expected
