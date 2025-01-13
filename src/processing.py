from typing import Any, Dict, List


def filter_by_state(transactions: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Функция фильтрует список транзакций по указанному состоянию.

    :param transactions: Список транзакций, где каждая транзакция представлена как словарь.
    :param state: Строка, указывающая состояние для фильтрации (по умолчанию 'EXECUTED').
    :return: Список транзакций, соответствующих указанному состоянию.
    """
    return [transaction for transaction in transactions if transaction.get('state') == state]


def sort_by_date(transactions: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список транзакций по дате.

    :param transactions: Список транзакций, где каждая транзакция представлена как словарь.
    :param descending: Параметр, указывающий порядок сортировки. По умолчанию True (убывание).
    :return: Новый список, отсортированный по дате.
    """
    return sorted(transactions, key=lambda x: x['date'], reverse=descending)


# Пример использования функций
if __name__ == "__main__":
    transactions = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

    # Вывод с состоянием по умолчанию 'EXECUTED'
    executed_transactions = filter_by_state(transactions)
    print("Транзакции со статусом 'EXECUTED':", executed_transactions)

    # Вывод с состоянием 'CANCELED'
    canceled_transactions = filter_by_state(transactions, 'CANCELED')
    print("Транзакции со статусом 'CANCELED':", canceled_transactions)

    # Пример входных данных для сортировки
    sorted_transactions_desc = sort_by_date(transactions)
    print("Отсортированные транзакции (убывание):", sorted_transactions_desc)

    sorted_transactions_asc = sort_by_date(transactions, descending=False)
    print("Отсортированные транзакции (возрастание):", sorted_transactions_asc)
