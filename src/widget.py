def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета.

    Аргументы:
    info: str - строка вида "Тип Номер".

    Возвращает:
    str - строка с замаскированным номером.
    """
    # Разделяем строку на тип и номер
    try:
        card_type, number_str = info.rsplit(" ", 1)
    except ValueError:
        raise ValueError("Некорректный формат данных. Ожидается: 'Тип Номер'.")

    # Проверяем, что номер состоит только из цифр
    if not number_str.isdigit():
        raise ValueError("Номер должен содержать только цифры.")

    # Проверяем длину номера
    if card_type.lower() == "счет":
        if len(number_str) < 10:
            raise ValueError("Номер счета должен содержать не менее 10 цифр.")
        mask = get_mask_account(number_str)  # Оставляем как строку
    else:
        if len(number_str) < 13 or len(number_str) > 19:
            raise ValueError("Номер карты должен содержать от 13 до 19 цифр.")
        mask = get_mask_card_number(number_str)  # Оставляем как строку

    return f"{card_type} {mask}"


def get_mask_account(number_str: str) -> str:
    """
    Маскирует номер счета, оставляя только последние 4 цифры.

    Аргументы:
    number_str: str - строка с номером счета.

    Возвращает:
    str - строка с замаскированным номером счета.
    """
    masked_length = len(number_str) - 4
    masked_part = '*' * masked_length
    return masked_part + number_str[-4:]


def get_mask_card_number(number_str: str) -> str:
    """
    Маскирует номер карты, оставляя только последние 4 цифры.

    Аргументы:
    number_str: str - строка с номером карты.

    Возвращает:
    str - строка с замаскированным номером карты.
    """
    return '*' * (len(number_str) - 4) + number_str[-4:]


def get_date(date_str: str) -> str:
    """
    Функция для преобразования даты из формата ISO в формат ДД.ММ.ГГГГ.

    Аргументы:
    date_str: str - строка с датой в формате "YYYY-MM-DDTHH:MM:SS.ssssss".

    Возвращает:
    str - строка с датой в формате "ДД.ММ.ГГГГ".
    """
    from datetime import datetime

    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")


# Примеры использования функций
if __name__ == "__main__":  # Исправлено здесь
    print(mask_account_card("Visa 7000792289606362"))  # Пример с картой
    print(mask_account_card("Счет 73654108430135874305"))  # Пример с номером счета
    print(get_date("2024-03-11T02:26:18.671407"))  # Пример преобразования даты
