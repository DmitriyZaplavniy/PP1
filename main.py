from masks import get_mask_account, get_mask_card_number


def main():
    # Пример использования функции маскировки номера карты
    card_number = 7000792289606362
    masked_card = get_mask_card_number(card_number)
    print(f"Замаскированный номер карты: {masked_card}")

    # Пример использования функции маскировки номера счета
    account_number = 73654108430135874305
    masked_account = get_mask_account(account_number)
    print(f"Замаскированный номер счета: {masked_account}")


if __name__ == "__main__":
    main()
