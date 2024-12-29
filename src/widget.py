from src.masks.masks import get_mask_card_number, get_mask_account  # Предполагаем, что эти функции уже реализованы в masks.py

def mask_account_card(info: str) -> str:
    """
    Функция для маскировки номера карты или счета.

    Аргументы:
    info: str - строка с типом и номером карты или счета.

    Возвращает:
    str - строка с замаскированным номером.
    """
    parts = info.rsplit(' ', 1)  # Разделяем строку на две части: все до последнего пробела и последнее слово
    if len(parts) != 2:
        raise ValueError("Некорректный формат входных данных")

    card_type = parts[0]  # Все, что до последнего пробела, считается типом карты
    number_str = parts[1]  # Последнее слово - это номер карты или счета

    try:
        number = int(number_str)  # Преобразуем номер в целое число
    except ValueError:
        raise ValueError("Номер карты или счета должен быть числом")

    # Проверка типа карты и вызов соответствующей функции маскировки
    if card_type.lower() in ["visa", "mastercard", "maestro"]:  # Добавьте другие типы карт по необходимости
        return get_mask_card_number(number)
    elif card_type.lower() == "счет":
        return get_mask_account(number)
    else:
        raise ValueError("Неизвестный тип карты или счета")


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
if __name__ == "__main__":  # Исправлено
    print(mask_account_card("Visa Classic 7000792289606361"))  # Пример с несколькими словами
    print(mask_account_card("Счет 73654108430135874305"))  # Вывод: Счет **4305
    print(get_date("2024-03-11T02:26:18.671407"))  # Вывод: 11.03.2024
