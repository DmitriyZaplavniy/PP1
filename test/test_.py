import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Фикстура для транзакций с валютами
@pytest.fixture
def transactions_with_currency():
    return [
        {
            "id": 1,
            "operationAmount": {
                "amount": "100.00",
                "currency": {"code": "USD"}
            }
        },
        {
            "id": 2,
            "operationAmount": {
                "amount": "200.00",
                "currency": {"code": "EUR"}
            }
        },
        {
            "id": 3,
            "operationAmount": {
                "amount": "150.00",
                "currency": {"code": "USD"}
            }
        },
        {
            "id": 4,
            "operationAmount": {
                "amount": "250.00",
                "currency": {"code": "GBP"}
            }
        }
    ]


# Параметризованный тест для фильтрации по валюте
@pytest.mark.parametrize("currency_code, expected_ids", [
    ("USD", [1, 3]),
    ("EUR", [2]),
    ("GBP", [4]),
    ("JPY", []),  # Нет транзакций в этой валюте
])
def test_filter_by_currency(transactions_with_currency, currency_code, expected_ids):
    filtered_transactions = list(filter_by_currency(transactions_with_currency, currency_code))
    filtered_ids = [transaction["id"] for transaction in filtered_transactions]
    assert filtered_ids == expected_ids


# Фикстура для транзакций без валюты (если это необходимо)
@pytest.fixture
def transactions_without_currency():
    return [
        {"operationType": "Перевод организации"},
        {"operationType": "Перевод со счета на счет"},
        {"operationType": "Перевод с карты на карту"},
        {"operationType": "Перевод организации"},
        {"operationType": "Перевод между счетами"},
    ]


@pytest.fixture
def transactions():
    return [
        {"operationType": "Перевод организации"},
        {"operationType": "Перевод со счета на счет"},
        {"operationType": "Перевод с карты на карту"},
        {"operationType": "Перевод организации"},
        {"operationType": "Перевод между счетами"},
    ]


def test_transaction_descriptions(transactions):
    descriptions = transaction_descriptions(transactions)

    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
        "Перевод между счетами"
    ]

    for expected in expected_descriptions:
        assert next(descriptions) == expected


def test_transaction_descriptions_empty():
    descriptions = transaction_descriptions([])

    with pytest.raises(StopIteration):
        next(descriptions)  # Ожидаем ошибку при попытке получить значение из пустого генератора


@pytest.fixture
def card_range():
    return (1, 5)


def test_card_number_format(card_range):
    expected_numbers = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005"
    ]

    generated_numbers = list(card_number_generator(*card_range))

    assert generated_numbers == expected_numbers


@pytest.mark.parametrize("start, stop, expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (10, 12, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"]),
])
def test_card_number_parametrization(start, stop, expected):
    generated_numbers = list(card_number_generator(start, stop))
    assert generated_numbers == expected
