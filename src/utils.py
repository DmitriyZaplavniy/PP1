import json
import os


def read_json_file(file_path):
    """Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях."""
    if not os.path.exists(file_path):
        return []

    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
        except json.JSONDecodeError:
            return []
