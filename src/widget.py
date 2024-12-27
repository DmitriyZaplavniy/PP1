# src/widget.py

def mask_account_card(info):
    """
    Функция для маскировки номера карты или счета.

    Аргументы:
    info: str - строка с типом и номером карты или счета.

    Возвращает:
    str - строка с замаскированным номером.
    """
    parts = info.split()
    card_type = " ".join(parts[:-1])
    number = parts[-1]

    if card_type.lower() in ["visa", "mastercard", "maestro"]:  # Добавьте другие типы карт по необходимости
        return f"{card_type} {number[:4]} {number[4:6]}** **** {number[-4:]}"
    elif card_type.lower() == "счет":
        return f"{card_type} **{number[-4:]}"
    else:
        raise ValueError("Неизвестный тип карты или счета")


def get_date(date_str):
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
if __name__ == "__main__":
    print(mask_account_card("Visa 7000792289606361"))  # Вывод: Visa 7000 79** **** 6361
    print(mask_account_card("Счет 73654108430135874305"))  # Вывод: Счет **4305
    print(get_date("2024-03-11T02:26:18.671407"))  # Вывод: 11.03.2024
