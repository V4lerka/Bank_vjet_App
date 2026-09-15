def get_mask_card_number(user_card_number: str) -> str:
    """Функция маскирует номер банковской карты"""
    if not isinstance(user_card_number, str):
        raise TypeError("Неверный тип введенных данных")
    elif user_card_number.strip().isdigit() and len(user_card_number.strip()) < 16:
        raise Exception("Номер карты должен содержать ровно 16 цифр, вы ввели меньше")
    elif user_card_number.strip().isdigit() and len(user_card_number.strip()) > 16:
        raise Exception("Номер карты должен содержать ровно 16 цифр, вы ввели больше")
    elif not user_card_number.strip().isdigit() and len(user_card_number.strip()) != 0:
        raise Exception("Номер карты должен содержать только цифры без пробелов")
    elif user_card_number.strip() == "":
        raise Exception("Вы ничего не ввели")
    return " ".join(
        [user_card_number.strip()[:4], f"{user_card_number.strip()[4:6]}**", "****", user_card_number.strip()[12:]])


def get_mask_account(user_account_number: str) -> str:
    """Функция маскирует номер банковского счета"""
    if not isinstance(user_account_number, str):
        raise TypeError("Неверный тип введенных данных")
    elif user_account_number.strip().isdigit() and len(user_account_number.strip()) < 4:
        raise Exception("Номер счета слишком короткий. Минимальная длина 4 цифры")
    elif not user_account_number.strip().isdigit() and len(user_account_number.strip()) != 0:
        raise Exception("Номер счета должен содержать только цифры без пробелов")
    elif user_account_number.strip() == "":
        raise Exception("Вы ничего не ввели")
    elif user_account_number.strip().isdigit() and len(user_account_number.strip()) == 4:
        return user_account_number.strip()[-4:]
    elif user_account_number.strip().isdigit() and len(user_account_number.strip()) == 5:
        return "".join(["*", user_account_number.strip()[-4:]])
    return "".join(["**", user_account_number.strip()[-4:]])
