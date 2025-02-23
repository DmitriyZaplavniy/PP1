import sys
from transaction_filter import filter_transactions_by_description, filter_transactions_by_status, categorize_transactions
from transaction_utils import load_transactions_from_json, load_transactions_from_csv, load_transactions_from_xlsx

def main():
    """Основная функция программы, которая управляет процессом работы с транзакциями."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    file_path = input("Введите путь к файлу с транзакциями (JSON/CSV/XLSX): ")

    # Загрузка транзакций в зависимости от формата файла
    if file_path.endswith('.json'):
        transactions = load_transactions_from_json(file_path)
    elif file_path.endswith('.csv'):
        transactions = load_transactions_from_csv(file_path)
    elif file_path.endswith('.xlsx'):
        transactions = load_transactions_from_xlsx(file_path)
    else:
        print("Неверный формат файла.")
        sys.exit()

    # Фильтрация по описанию
    search_string = input("Введите строку для поиска в описании транзакций: ")
    filtered_transactions = filter_transactions_by_description(transactions, search_string)

    print(f"Найдено {len(filtered_transactions)} транзакций по описанию:")
    for transaction in filtered_transactions:
        print(transaction)

    # Фильтрация по статусу
    status = input("Хотите отфильтровать транзакции по статусу? Введите статус (например, 'завершено', 'ожидание') или 'нет' для пропуска: ")
    if status.lower() != 'нет':
        filtered_transactions = filter_transactions_by_status(filtered_transactions, status)
        print(f"Найдено {len(filtered_transactions)} транзакций с статусом '{status}':")
        for transaction in filtered_transactions:
            print(transaction)

    # Категоризация транзакций
    category_count = categorize_transactions(transactions)
    print("Количество операций по категориям:")
    for category, count in category_count.items():
        print(f"{category}: {count}")

if __name__ == "__main__":
    main()
