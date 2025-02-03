import logging
from functools import wraps


def setup_logging(filename=None):
    """Настройка логирования."""
    if filename:
        logging.basicConfig(filename=filename, level=logging.INFO,
                            format='%(asctime)s - %(message)s')
    else:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s')


def log(filename=None):
    """Декоратор для логирования начала и конца выполнения функции."""
    setup_logging(filename)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logging.info(f"Starting {func.__name__} with args: {args}, kwargs: {kwargs}")
                result = func(*args, **kwargs)
                logging.info(f"{func.__name__} completed successfully.")
                return result
            except Exception as e:
                error_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                logging.error(error_message)
                print(error_message)  # Печатаем ошибку в консоль
                raise

        return wrapper

    return decorator
