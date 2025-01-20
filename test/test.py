import unittest
from typing import Any, Dict, List

import pytest
from parameterized import parameterized

from masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card


# Фикстура для генерации данных для тестирования карт
@pytest.fixture
def card_numbers():
    return [
        (1234567812345678, "1234 5678 **** 5678"),
        (4000123412341234, "4000 1234 **** 1234"),
        (12345678, ValueError("Номер карты должен содержать 16 цифр.")),
        (12345678901234567890, ValueError("Номер карты должен содержать 16 цифр.")),
        ("", ValueError("Номер карты должен содержать 16 цифр."))
    ]


# Параметризованный тест для проверки номеров карт
@pytest.mark.parametrize("card_number, expected", [
    (1234567812345678, "1234 5678 **** 5678"),
    (4000123412341234, "4000 1234 **** 1234")
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


# Тест на выброс исключений для некорректных номеров карт
@pytest.mark.parametrize("card_number", [
    12345678,
    12345678901234567890,
    ""
])
def test_get_mask_card_number_exceptions(card_number):
    with pytest.raises(ValueError) as excinfo:
        get_mask_card_number(card_number)
    assert str(excinfo.value) == "Номер карты должен содержать 16 цифр."


# Фикстура для генерации данных для тестирования счетов
@pytest.fixture
def account_numbers():
    return [
        (1234567890, "7890"),
        (987654321, "4321"),
        (123, ValueError("Номер счета должен содержать хотя бы 4 цифры.")),
        ("", ValueError("Номер счета должен содержать хотя бы 4 цифры."))
    ]


# Параметризованный тест для проверки номеров счетов
@pytest.mark.parametrize("account_number, expected", [
    (1234567890, "7890"),
    (987654321, "4321")
])
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected


# Тест на выброс исключений для некорректных номеров счетов
@pytest.mark.parametrize("account_number", [
    123,
    ""
])
def test_get_mask_account_exceptions(account_number):
    with pytest.raises(ValueError) as excinfo:
        get_mask_account(account_number)
    assert str(excinfo.value) == "Номер счета должен содержать хотя бы 4 цифры."


# Запуск тестов
if __name__ == "__main__":
    pytest.main()


# Фикстура для создания данных
@pytest.fixture
def account_card_data():
    return [
        ("Visa 7000792289606362", "Visa ************6362"),
        ("Счет 73654108430135874305", "Счет ****************5305"),
        ("Visa 123", ValueError),  # Номер карты слишком короткий
        ("Счет 123456789", ValueError),  # Номер счета слишком короткий
        ("Счет ABCDEFGHIJ", ValueError),  # Неверный формат номера
    ]


@pytest.mark.parametrize("info, expected", [
    ("Visa 7000792289606362", "Visa ************6362"),
    ("Счет 73654108430135874305", "Счет ****************4305"),
])
def test_mask_account_card_valid(info, expected):
    assert mask_account_card(info) == expected


@pytest.mark.parametrize("info", [
    "Visa 123",  # Номер карты слишком короткий
    "Счет 123456789",  # Номер счета слишком короткий
    "Счет ABCDEFGHIJ",  # Неверный формат номера
])
def test_mask_account_card_invalid(info):
    with pytest.raises(ValueError):
        mask_account_card(info)


@pytest.mark.parametrize("date_str, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
])
def test_get_date_valid(date_str, expected):
    assert get_date(date_str) == expected


@pytest.mark.parametrize("date_str", [
    "Некорректная дата",  # Неверный формат даты
])
def test_get_date_invalid(date_str):
    with pytest.raises(ValueError):
        get_date(date_str)


if __name__ == "__main__":  # Исправлено здесь
    pytest.main()


# Ваши функции
def filter_by_state(transactions: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    return [transaction for transaction in transactions if transaction.get('state') == state]


def sort_by_date(transactions: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    return sorted(transactions, key=lambda x: x['date'], reverse=descending)


# Класс для тестирования
class TestTransactionFunctions(unittest.TestCase):

    def setUp(self):
        self.transactions = [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ]

    @parameterized.expand([
        ('EXECUTED', [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
        ]),
        ('CANCELED', [
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ]),
        ('PENDING', [])
    ])
    def test_filter_by_state(self, state, expected):
        result = filter_by_state(self.transactions, state)
        self.assertEqual(result, expected)

    def test_sort_by_date_descending(self):
        result = sort_by_date(self.transactions)
        expected = [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
        ]
        self.assertEqual(result, expected)

    def test_sort_by_date_ascending(self):
        result = sort_by_date(self.transactions, descending=False)
        expected = [
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
        ]
        self.assertEqual(result, expected)

    @parameterized.expand([
        ([{'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01T10:00:00'},
          {'id': 2, 'state': 'EXECUTED', 'date': '2023-01-01T10:00:00'},
          {'id': 3, 'state': 'CANCELED', 'date': '2023-01-01T10:00:00'}],
         [{'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01T10:00:00'},
          {'id': 2, 'state': 'EXECUTED', 'date': '2023-01-01T10:00:00'},
          {'id': 3, 'state': 'CANCELED', 'date': '2023-01-01T10:00:00'}])
    ])
    def test_sort_by_date_with_same_dates(self, transactions_with_same_dates, expected):
        result = sort_by_date(transactions_with_same_dates)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
