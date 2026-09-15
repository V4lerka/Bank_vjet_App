def get_mask_card_number(user_card_number: str) -> str:
    """Функция маскирует номер банковской карты"""
    if user_card_number.strip().isdigit() and len(user_card_number.strip()) != 16:
        mask_card_number = f"Номер карты должен содержать ровно 16 цифр, вы ввели {len(user_card_number.strip())}"
    elif not user_card_number.strip().isdigit() and len(user_card_number.strip()) != 0:
        mask_card_number = "Номер карты должен содержать только цифры, к тому же без пробелов"
    elif user_card_number.strip() == "":
        mask_card_number = "Вы ничего не ввели"
    elif user_card_number.strip().isdigit() and len(user_card_number.strip()) == 16:
        mask_card_number = " ".join(
            [user_card_number.strip()[:4], f"{user_card_number.strip()[4:6]}**", "****", user_card_number.strip()[12:]]
        )
    else:
        mask_card_number = "Непредвиденная ошибка ввода. Повторите ввод"
    return mask_card_number


def get_mask_account(user_account_number: str) -> str:
    """Функция маскирует номер банковского счета"""
    if user_account_number.strip().isdigit() and len(user_account_number.strip()) >= 6:
        account_number_hide = "".join(["**", user_account_number.strip()[-4:]])
    elif user_account_number.strip().isdigit() and len(user_account_number.strip()) == 4:
        account_number_hide = user_account_number.strip()[-4:]
    elif user_account_number.strip().isdigit() and len(user_account_number.strip()) == 5:
        account_number_hide = "".join(["*", user_account_number.strip()[-4:]])
    elif user_account_number.strip().isdigit() and len(user_account_number.strip()) < 4:
        account_number_hide = "Номер счета слишком короткий. Минимальная длина 4 цифры"
    elif not user_account_number.strip().isdigit() and len(user_account_number.strip()) != 0:
        account_number_hide = "Номер счета должен содержать только цифры, к тому же без пробелов"
    elif user_account_number.strip() == "":
        account_number_hide = "Вы ничего не ввели"
    else:
        account_number_hide = "Непредвиденная ошибка ввода. Повторите ввод"
    return account_number_hide
