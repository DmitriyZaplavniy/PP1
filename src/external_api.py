import requests

API_KEY = "KOf4uCHOu9knq4AlkUEnEHAsf8qYdVGa"  # Замените на ваш ключ API
BASE_URL = 'https://api.apilayer.com/exchangerates_data'


def convert_to_rub(amount, currency):
    if currency == "RUB":
        return float(amount)

    response = requests.get(f"{BASE_URL}/latest?base={currency}&apikey={API_KEY}")

    if response.status_code != 200:
        raise Exception("Ошибка при обращении к API.")

    rates = response.json().get('rates', {})

    if 'RUB' in rates:
        return float(amount) * rates['RUB']
    else:
        raise ValueError("Курс валюты не найден.")
