import requests
import os


def convert_currency(transaction, currency):
    """Конвертирует сумму транзакции в рубли, если валюта USD или EUR."""
    amount = transaction.get('amount')

    if currency not in ['USD', 'EUR']:
        return float(amount)

    api_key = os.getenv('API_KEY')  # Получение API-ключа из переменной окружения
    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"

    headers = {
        "apikey": api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception("Ошибка получения данных о курсе валют")

    data = response.json()

    if 'error' in data:
        raise Exception("Ошибка получения данных о курсе валют")

    rate = data['rates']['RUB']
    return float(amount) * rate

