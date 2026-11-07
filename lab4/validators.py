"""Модуль валидации ввода пользователя."""

from constants import (
    SECTION_DIM_MIN, SECTION_DIM_MAX,
    MOMENT_MIN, MOMENT_MAX,
    ALLOWABLE_STRESS_MIN, ALLOWABLE_STRESS_MAX
)
from logger import log_error


def validate_float_input(prompt: str, min_val: float, max_val: float) -> float:
    """
    Запрашивает число с плавающей точкой у пользователя и проверяет 
    нахождение значения в заданном диапазоне [min_val, max_val].
    """
    while True:
        try:
            val_str = input(prompt).strip()
            val = float(val_str)
            if min_val <= val <= max_val:
                return val
            else:
                msg = f"Значение {val} выходит за допустимый диапазон [{min_val}..{max_val}]."
                print(f"Ошибка: {msg}")
                log_error(msg)
        except ValueError:
            msg = f"Некорректный ввод '{val_str}'. Ожидалось число."
            print(f"Ошибка: {msg}")
            log_error(msg)