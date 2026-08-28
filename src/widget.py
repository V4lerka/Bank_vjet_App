from src.masks import get_mask_account, get_mask_card_number
import re
from datetime import datetime

def mask_account_card(user_bank_data: str) -> str:
    """Функция принимает информацию от пользователя о номере банковского счета или карты в виде строки и возвращает замаскированные банковские данные"""
    result = re.findall(r"[0-9]+", user_bank_data)
    bank_number = "".join(result)
    if user_bank_data.lower().strip().startswith("счет"):
        masked_number = get_mask_account(bank_number)
        masked_bank_data = f"Счет {masked_number}"
    else:
        masked_number = get_mask_card_number(bank_number)
        result = re.findall(r"[A-Z][a-z]+", user_bank_data.strip())
        card_name = " ".join(result)
        masked_bank_data = f"{card_name} {masked_number}"
    return masked_bank_data


def get_date(date_iso: str) -> str:
    """Функция принимает строку с датой в формате <2024-03-11T02:26:18.671407> и возвращает строку с датой в формате
<ДД.ММ.ГГГГ>"""
    date_object = datetime.fromisoformat(date_iso)
    norm_date = date_object.strftime("%d.%m.%Y")
    return norm_date