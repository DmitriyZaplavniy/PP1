import json
import pandas as pd

def load_transactions_from_json(file_path):
    """Загружает транзакции из JSON-файла."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def load_transactions_from_csv(file_path):
    """Загружает транзакции из CSV-файла."""
    return pd.read_csv(file_path).to_dict(orient='records')

def load_transactions_from_xlsx(file_path):
    """Загружает транзакции из XLSX-файла."""
    return pd.read_excel(file_path).to_dict(orient='records')
