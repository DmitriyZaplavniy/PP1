def get_mask_card_number(card_number: int) -> str:
    """
    Возвращает замаскированный номер карты в формате XXXX XX** **** XXXX.

    :param card_number: Номер карты в виде числа.
    :return: Замаскированный номер карты.
    """
    card_number_str = str(card_number)
    masked_card_number = f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    return masked_card_number


def get_mask_account(account_number: int) -> str:
    """
    Возвращает замаскированный номер счета в формате **XXXX.

    :param account_number: Номер счета в виде числа.
    :return: Замаскированный номер счета.
    """
    account_number_str = str(account_number)
    masked_account_number = f"**{account_number_str[-4:]}"
    return masked_account_number
