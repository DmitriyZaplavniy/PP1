from src.utils import read_json_file
from src.external_api import convert_to_rub


def main():
    transactions = read_json_file('data/operations.json')

    for transaction in transactions:
        amount = transaction.get('amount')
        currency = transaction.get('currency')

        if amount is not None and currency is not None:
            try:
                amount_in_rub = convert_to_rub(amount, currency)
                print(f"Сумма транзакции: {amount_in_rub} RUB")
            except Exception as e:
                print(f"Ошибка конвертации: {e}")


if __name__ == "__main__":
    main()
