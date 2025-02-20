import pytest
from bank_transactions.transaction_filter import filter_transactions_by_description, categorize_transactions


def test_filter_transactions_by_description():
    transactions = [
        {'description': 'Покупка в магазине', 'amount': 100},
        {'description': 'Перевод на карту', 'amount': 200},
        {'description': 'Оплата за интернет', 'amount': 300}
    ]

    result = filter_transactions_by_description(transactions, 'магазин')
    assert len(result) == 1
    assert result[0]['description'] == 'Покупка в магазине'


def test_categorize_transactions():
    transactions = [
        {'description': 'Покупка в магазине', 'amount': 100, 'category': 'Shopping'},
        {'description': 'Оплата за интернет', 'amount': 300, 'category': 'Utilities'},
        {'description': 'Покупка еды', 'amount': 50, 'category': 'Food'},
        {'description': 'Оплата за свет', 'amount': 150, 'category': 'Utilities'}
    ]

    result = categorize_transactions(transactions)
    assert result == {'Shopping': 1, 'Utilities': 2, 'Food': 1}
