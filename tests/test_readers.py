from unittest.mock import mock_open, patch
from src.readers import csv_reader, excel_reader
import pytest

# Тесты csv_reader
def test_csv_reader():
    """Успешный тест чтения файла без данных о транзакциях"""
    file_content = "id;state;date;amount;currency_name;from;to;description\n"
    mocked_file = mock_open(read_data=file_content)
    with patch("builtins.open", mocked_file):
        result = csv_reader("fake.csv")
    assert result == []


def test_csv_reader2():
    """Успешный тест чтения пустого файла"""
    file_content = ""
    mocked_file = mock_open(read_data=file_content)
    with patch("builtins.open", mocked_file):
        result = csv_reader("fake.csv")
    assert result == []


def test_csv_reader3(csv_data_ok):
    """Успешный тест чтения файла"""
    file_content = "id;amount;currency\n1;100.50;RUB\n2;250.00;USD"
    mocked_file = mock_open(read_data=file_content)
    with patch("builtins.open", mocked_file):
        result = csv_reader("fake.csv")
    assert result == csv_data_ok


def test_csv_reader_wrong_extension():
    """Тест вызова Exception при неверном расширении файла."""
    with pytest.raises(Exception) as e:
        csv_reader("data.txt")
    assert str(e.value) == "Формат файла не поддерживается"


def test_csv_reader_file_not_found(capsys):
    """Тест, когда файла нет в папке."""
    result = csv_reader("fake.csv")
    assert result == []
    captured = capsys.readouterr()
    assert "Ошибка:" in captured.out


# Тесты excel_reader

def test_excel_reader(capsys):
    """Тест, когда файла нет в папке."""
    result = excel_reader("fake.xlsx")
    assert result == []
    captured = capsys.readouterr()
    assert "Ошибка:" in captured.out


def test_excel_reader_wrong_extension():
    """Тест вызова Exception при неверном расширении файла."""
    with pytest.raises(Exception) as e:
        excel_reader("data.txt")
    assert str(e.value) == "Формат файла не поддерживается"


def test_excel_reader2():
    """Успешный тест чтения пустого файла"""
    file_content = ""
    mocked_file = mock_open(read_data=file_content)
    with patch("builtins.open", mocked_file):
        result = excel_reader("fake.xlsx")
    assert result == []
