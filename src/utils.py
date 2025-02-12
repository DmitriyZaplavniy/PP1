import json
import os
import logging

# Настройка логирования для модуля utils
logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler('logs/utils.log', mode='w', encoding='utf-8')  # Указываем кодировку UTF-8
file_handler.setLevel(logging.DEBUG)

# Настройка форматирования логов
file_formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def read_json_file(file_path):
    """Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях."""
    if not os.path.exists(file_path):
        logger.warning(f'Файл не найден: {file_path}')
        return []

    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            if isinstance(data, list):
                logger.info(f'Успешно прочитан файл: {file_path}')
                return data
            else:
                logger.error(f'Файл не содержит список: {file_path}')
                return []
        except json.JSONDecodeError as e:
            logger.error(f'Ошибка декодирования JSON в файле {file_path}: {e}')
            return []


# Пример использования функции
if __name__ == "__main__":
    transactions = read_json_file('path/to/your/file.json')
    print(transactions)
