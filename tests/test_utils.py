import json
from unittest.mock import mock_open, patch
from src.utils import convert_json_to_list
from tests.conftest import not_list


def test_convert_json_to_list(capsys):
    file_content = ""
    mocked_file = mock_open(read_data=file_content)
    with patch("builtins.open", mocked_file):
        result = convert_json_to_list("fake_path.json")
    assert result == []
    captured = capsys.readouterr()
    assert captured.out == "Формат не соответствует JSON или файл пустой\n"


def test_convert_json_to_list2(not_list, capsys):
    json_not_list = json.dumps(not_list)
    file_content = f"{json_not_list}"
    mocked_file = mock_open(read_data=file_content)
    with patch("builtins.open", mocked_file):
        result = convert_json_to_list("fake_path.json")
    assert result == []
    captured = capsys.readouterr()
    assert captured.out == "Тип данных в файле не является списком\n"


def test_convert_json_to_list3(not_json_transactions, capsys):
    file_content = f"{not_json_transactions}"
    mocked_file = mock_open(read_data=file_content)
    with patch("builtins.open", mocked_file):
        result = convert_json_to_list("fake_path.json")
    assert result == []
    captured = capsys.readouterr()
    assert captured.out == "Формат не соответствует JSON или файл пустой\n"


def test_convert_json_to_list4(capsys):
    result = convert_json_to_list("fake_path.json")
    assert result == []
    captured = capsys.readouterr()
    assert captured.out == "Файл не найден по указанному пути\n"


def test_convert_json_to_list5(json_transactions):
    json_transactions_json = json.dumps(json_transactions)
    file_content = f"{json_transactions_json}"
    mocked_file = mock_open(read_data=file_content)
    with patch("builtins.open", mocked_file):
        result = convert_json_to_list("fake_path.json")
    assert result == json_transactions
