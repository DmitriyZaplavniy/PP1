import sys
import os

# Добавляем путь к src в sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))  # Исправлено: __file__ вместо file

from src.masks.masks import get_mask_card_number, get_mask_account


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
        mask = get_mask_account(int(number_str))
    else:
        if len(number_str) < 13:
            raise ValueError("Номер карты должен содержать не менее 13 цифр.")
        mask = get_mask_card_number(int(number_str))

    return f"{card_type} {mask}"


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

