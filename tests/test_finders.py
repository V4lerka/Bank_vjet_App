from src.finders import process_bank_search, process_bank_operations


def test_process_bank_search1(transactions_data):
    assert process_bank_search(transactions_data, "перевод") == [{"id": 650703,
                                                                  "status": "EXECUTED",
                                                                  "date": "2023-09-05T11:30:32Z",
                                                                  "Amount": 16210,
                                                                  "currency_name": "Sol",
                                                                  "currency_code": "PEN",
                                                                  "from": "Счет 58803664561298323391",
                                                                  "to": "Счет 39745660563456619397",
                                                                  "description": "Перевод организации"},
                                                                 {"id": 650703,
                                                                  "status": "EXECUTED",
                                                                  "date": "2023-09-05T11:30:32Z",
                                                                  "Amount": 16210,
                                                                  "currency_name": "Sol",
                                                                  "currency_code": "PEN",
                                                                  "from": "Счет 58803664561298323391",
                                                                  "to": "Счет 39745660563456619397",
                                                                  "description": "Перевод организации"}]


def test_process_bank_search2(transactions_data, capsys):
    assert process_bank_search(transactions_data, "покупка") == []
    captured = capsys.readouterr()
    assert captured.out == "По вашему запросу ничего не найдено\n"


def test_process_bank_search3(capsys):
    assert process_bank_search([], "Перевод") == []
    captured = capsys.readouterr()
    assert captured.out == "Список транзакций пуст, анализ не возможен\n"


def test_process_bank_operations1(transactions_data):
    assert process_bank_operations(transactions_data, ["Перевод", "Оплата", "Ипотека", "Покупка"]) == {'Перевод': 2,
                                                                                                       'Оплата': 1,
                                                                                                       'Ипотека': 1,
                                                                                                       'Покупка': 0}


def test_process_bank_operations2(transactions_data, capsys):
    assert process_bank_operations(transactions_data, ["покупка"]) == {"покупка": 0}
    captured = capsys.readouterr()
    assert captured.out == "По вашему запросу ничего не найдено\n"


def test_process_bank_operations3(capsys):
    assert process_bank_operations([], ["Перевод"]) == {}
    captured = capsys.readouterr()
    assert captured.out == "Список транзакций пуст, анализ не возможен\n"
