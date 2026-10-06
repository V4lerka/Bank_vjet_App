import os

import requests
from dotenv import load_dotenv
from requests import RequestException

load_dotenv()


def show_transactions_amount(transaction: dict) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float.
    Если валюта отличная от RUB, конвертирует её через API.
    В случае ошибки запроса возвращает 0.0"""
    if type(transaction) is not dict:
        raise TypeError("Неверный формат входных данных")
    operation_amount = transaction.get("operationAmount", {})
    amount_raw = operation_amount.get("amount")
    if amount_raw is None:
        return 0.0
    currency = operation_amount.get("currency", {}).get("code")
    amount = float(amount_raw)
    if not currency:
        return 0.0
    if currency and currency != "RUB":
        url = "https://api.apilayer.com/exchangerates_data/convert"
        api_key = os.getenv("API_KEY")
        headers = {"apikey": api_key}
        params = {"to": "RUB", "from": f"{currency}", "amount": amount}
        try:
            response = requests.get(url, headers=headers, params=params, timeout=3)
            response.raise_for_status()
            data = response.json()
            amount = data.get("result")
            if amount is None:
                return 0.0
        except RequestException as e:
            print(f"Ошибка при конвертации валюты: {e}")
            return 0.0
    return amount
