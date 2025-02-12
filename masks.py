import logging
import os

# Создаем папку logs, если она не существует
if not os.path.exists('logs'):
    os.makedirs('logs')

# Настройка логирования для модуля masks
logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler('logs/masks.log', mode='w', encoding='utf-8')  # Указываем кодировку UTF-8
file_handler.setLevel(logging.DEBUG)

# Настройка форматирования логов
file_formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    try:
        card_number_str = str(card_number)

        if len(card_number_str) != 16:
            raise ValueError("Номер карты должен содержать 16 цифр.")

        masked_card_number = f"{card_number_str[:4]} {card_number_str[4:8]} **** {card_number_str[-4:]}"

        # Логируем успешный случай
        logger.info(f'Успешно замаскирован номер карты: {masked_card_number}')

        return masked_card_number
    except Exception as e:
        # Логируем ошибку
        logger.error(f'Ошибка при замене номера карты: {e}')
        raise


def get_mask_account(account_number: int) -> str:
    try:
        account_number_str = str(account_number)

        if len(account_number_str) < 4:
            raise ValueError("Номер счета должен содержать хотя бы 4 цифры.")

        # Возвращаем только последние 4 цифры
        masked_account_number = account_number_str[-4:]

        # Логируем успешный случай
        logger.info(f'Успешно замаскирован номер счета: {masked_account_number}')

        return masked_account_number
    except Exception as e:
        # Логируем ошибку
        logger.error(f'Ошибка при замене номера счета: {e}')
        raise


# Пример использования функций
if __name__ == "__main__":  # Исправлено имя на __name__
    try:
        print(get_mask_card_number(1234567812345678))
    except ValueError as ve:
        print(ve)

    try:
        print(get_mask_account(123456))
    except ValueError as ve:
        print(ve)
