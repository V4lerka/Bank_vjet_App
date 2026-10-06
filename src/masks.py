import logging

from src.utils import file_handler

masks_logger = logging.getLogger(__name__)
masks_logger.addHandler(file_handler)
masks_logger.setLevel(logging.DEBUG)


def get_mask_card_number(user_card_number: str) -> str:
    """Функция маскирует номер банковской карты"""
    if not isinstance(user_card_number, str):
        masks_logger.error("Произошла ошибка в типе данных")
        raise TypeError("Неверный тип введенных данных")
    elif user_card_number.strip().isdigit() and len(user_card_number.strip()) < 16:
        masks_logger.error("Ошибка длины номера карты")
        raise Exception("Номер карты должен содержать ровно 16 цифр, вы ввели меньше")
    elif user_card_number.strip().isdigit() and len(user_card_number.strip()) > 16:
        masks_logger.error("Ошибка длины номера карты")
        raise Exception("Номер карты должен содержать ровно 16 цифр, вы ввели больше")
    elif not user_card_number.strip().isdigit() and len(user_card_number.strip()) != 0:
        masks_logger.error("Ошибка номера карты: содержит посторонние символы")
        raise Exception("Номер карты должен содержать только цифры без пробелов")
    elif user_card_number.strip() == "":
        masks_logger.error("Ошибка: пустой ввод")
        raise Exception("Вы ничего не ввели")
    masks_logger.info("Функция 'get_mask_card_number' успешно завершила работу")
    return " ".join(
        [user_card_number.strip()[:4], f"{user_card_number.strip()[4:6]}**", "****", user_card_number.strip()[12:]]
    )


def get_mask_account(user_account_number: str) -> str:
    """Функция маскирует номер банковского счета"""
    if not isinstance(user_account_number, str):
        masks_logger.error("Произошла ошибка в типе данных")
        raise TypeError("Неверный тип введенных данных")
    elif user_account_number.strip().isdigit() and len(user_account_number.strip()) < 4:
        masks_logger.error("Ошибка длины номера счета")
        raise Exception("Номер счета слишком короткий. Минимальная длина 4 цифры")
    elif not user_account_number.strip().isdigit() and len(user_account_number.strip()) != 0:
        masks_logger.error("Ошибка номера счета: содержит посторонние символы")
        raise Exception("Номер счета должен содержать только цифры без пробелов")
    elif user_account_number.strip() == "":
        masks_logger.error("Ошибка: пустой ввод")
        raise Exception("Вы ничего не ввели")
    elif user_account_number.strip().isdigit() and len(user_account_number.strip()) == 4:
        masks_logger.info("Функция 'get_mask_account' успешно завершила работу")
        return user_account_number.strip()[-4:]
    elif user_account_number.strip().isdigit() and len(user_account_number.strip()) == 5:
        masks_logger.info("Функция 'get_mask_account' успешно завершила работу")
        return "".join(["*", user_account_number.strip()[-4:]])
    masks_logger.info("Функция 'get_mask_account' успешно завершила работу")
    return "".join(["**", user_account_number.strip()[-4:]])
