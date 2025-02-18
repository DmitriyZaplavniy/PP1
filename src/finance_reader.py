import pandas as pd


def read_transactions_from_csv(file_path):
    """Считывает финансовые транзакции из CSV файла.

    Args:
        file_path (str): Путь к файлу CSV.

    Returns:
        list: Список словарей с транзакциями.
    """
    df = pd.read_csv(file_path)
    return df.to_dict(orient='records')


def read_transactions_from_excel(file_path):
    """Считывает финансовые транзакции из Excel файла.

    Args:
        file_path (str): Путь к файлу Excel.

    Returns:
        list: Список словарей с транзакциями.
    """
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')


# Пример использования
csv_file_path = r"C:UsersdimaPycharmProjectsPP1\transactions.csv"
excel_file_path = r"C:UsersdimaPycharmProjectsPP1\transactions_excel.xlsx"

csv_transactions = read_transactions_from_csv(csv_file_path)
excel_transactions = read_transactions_from_excel(excel_file_path)

print(csv_transactions)
print(excel_transactions)
