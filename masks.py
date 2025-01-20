def get_mask_card_number(card_number: int) -> str:
    card_number_str = str(card_number)

    if len(card_number_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр.")

    masked_card_number = f"{card_number_str[:4]} {card_number_str[4:8]} **** {card_number_str[-4:]}"
    return masked_card_number


def get_mask_account(account_number: int) -> str:
    account_number_str = str(account_number)

    if len(account_number_str) < 4:
        raise ValueError("Номер счета должен содержать хотя бы 4 цифры.")

    # Возвращаем только последние 4 цифры
    masked_account_number = account_number_str[-4:]
    return masked_account_number
