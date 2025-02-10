import logging
from functools import wraps

import pytest

# Настройка логирования
logging.basicConfig(level=logging.INFO)


def log():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logging.info(f"Starting {func.__name__} with args: {args}, kwargs: {kwargs}")
            try:
                result = func(*args, **kwargs)
                logging.info(f"{func.__name__} completed successfully.")
                return result
            except Exception as e:
                logging.error(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                raise
        return wrapper
    return decorator


@log()
def add(x, y):
    return x + y


@log()
def divide(x, y):
    return x / y  # Может вызвать деление на ноль


def test_successful_function(caplog):
    with caplog.at_level(logging.INFO):  # Убедитесь, что мы находимся на уровне INFO
        result = add(1, 2)
    assert result == 3
    assert "Starting add with args: (1, 2), kwargs: {}" in caplog.text
    assert "add completed successfully." in caplog.text


def test_error_function(caplog):
    with caplog.at_level(logging.ERROR):  # Убедитесь, что мы находимся на уровне ERROR
        with pytest.raises(ZeroDivisionError):
            divide(1, 0)

    assert "divide error: division by zero. Inputs: (1, 0), {}" in caplog.text
