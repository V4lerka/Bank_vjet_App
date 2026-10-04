import pytest
from src.external_api import show_transactions_amount
from unittest.mock import Mock, patch
from requests import RequestException
from tests.conftest import response_api, response_api_no_result


def test_show_transactions_amount(non_dict_transaction):
    with pytest.raises(TypeError) as e:
        show_transactions_amount(non_dict_transaction)
    assert str(e.value) == "Неверный формат входных данных"


@pytest.mark.parametrize("transaction, expected", [
    ({
         "id": 441945886,
         "state": "EXECUTED",
         "date": "2019-08-26T10:50:58.294041",
         "description": "Перевод организации",
         "from": "Maestro 1596837868705199",
         "to": "Счет 64686473678894779589"
     }, 0.0),
    ({
         "id": 441945886,
         "state": "EXECUTED",
         "date": "2019-08-26T10:50:58.294041",
         "operationAmount": {
             "amount": "31957.58",
             "currency": {
                 "name": "руб."}
         },
         "description": "Перевод организации",
         "from": "Maestro 1596837868705199",
         "to": "Счет 64686473678894779589"
     }, 0.0),
    ({
         "id": 441945886,
         "state": "EXECUTED",
         "date": "2019-08-26T10:50:58.294041",
         "operationAmount": {
             "amount": "31957.58",
             "currency": {
                 "name": "руб.",
                 "code": "RUB"
             }
         },
         "description": "Перевод организации",
         "from": "Maestro 1596837868705199",
         "to": "Счет 64686473678894779589"
     }, 31957.58)])
def test_show_transactions_amount2(transaction, expected):
    assert show_transactions_amount(transaction) == expected


def test_show_transactions_amount_api(transaction_ok_usd, response_api):
    """Успешный ответ от API: конвертация USD в RUB."""
    mock_response = Mock()
    mock_response.json.return_value = response_api
    with patch("requests.get") as mock_get:
        mock_get.return_value = mock_response
        assert show_transactions_amount(transaction_ok_usd) == 35758.0
        mock_get.assert_called_once()

def test_show_transactions_amount_api2(transaction_ok_usd, response_api_no_result):
    """Сервер ответил (код 200), но конвертация не прошла (result отсутствует)"""
    mock_response = Mock()
    mock_response.json.return_value = response_api_no_result
    with patch("requests.get") as mock_get:
        mock_get.return_value = mock_response
        assert show_transactions_amount(transaction_ok_usd) == 0.0
        mock_get.assert_called_once()

def test_show_transactions_amount_api_failed(transaction_ok_usd, capsys):
    """Тест ошибочных запросов"""
    def raise_http_error():
        raise RequestException("Ошибка сервера или неверный API-ключ")
    mock_response = Mock()
    mock_response.raise_for_status = raise_http_error
    with patch("requests.get") as mock_get:
        mock_get.return_value = mock_response
        result = show_transactions_amount(transaction_ok_usd)
        assert result == 0.0
        captured = capsys.readouterr()
        assert "Ошибка при конвертации валюты" in captured.out