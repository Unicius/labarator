"""Модуль логирования ошибок ввода."""

import logging

# Настройка логирования в файл
logging.basicConfig(
    filename='input_errors.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8',
    level=logging.WARNING
)

def log_error(message: str) -> None:
    """Логирует сообщение об ошибке ввода."""
    logging.warning(message)