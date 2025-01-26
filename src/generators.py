# Определение функции фильтрации
def filter_by_currency(transactions, currency_code):
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions):
    """
    Генератор, который возвращает описание каждой транзакции.

    :param transactions: Список словарей, представляющих транзакции.
    :yield: Описание операции.
    """
    for transaction in transactions:
        operation_type = transaction.get("operationType", "Неизвестная операция")
        yield operation_type


def card_number_generator(start, stop):
    for number in range(start, stop + 1):
        # Форматируем номер карты в виде XXXX XXXX XXXX XXXX
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[8:12] + " " + f"{number:016d}"[12:16]
