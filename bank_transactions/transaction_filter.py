import re
from collections import Counter


def filter_transactions_by_description(transactions, search_string):
    """
    Фильтрует транзакции по описанию с использованием регулярных выражений.

    :param transactions: Список словарей с транзакциями.
    :param search_string: Строка для поиска в описании транзакций.
    :return: Список словарей с отфильтрованными транзакциями.
    """
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction['description'])]


def categorize_transactions(transactions):
    """
    Подсчитывает количество банковских операций по категориям.

    :param transactions: Список словарей с транзакциями.
    :return: Словарь с количеством операций по категориям.
    """
    categories = [transaction['category'] for transaction in transactions if 'category' in transaction]
    return dict(Counter(categories))
