import os

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_currency(transaction):
    """Конвертирует сумму транзакции в рубли, если валюта USD или EUR."""
    amount = transaction.get('amount')
    currency = transaction.get('currency')

    if currency not in ['USD', 'EUR']:
        return float(amount)

    api_key = os.getenv('API_KEY')  # Получение API-ключа из переменной окружения
    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"

    headers = {
        "apikey": api_key
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    if 'error' in data:
        raise Exception("Ошибка получения данных о курсе валют")

    rate = data['rates']['RUB']
    return float(amount) * rate
