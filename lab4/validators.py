from constants import (
    DIMENSION_MIN, DIMENSION_MAX,
    MOMENT_MIN, MOMENT_MAX,
    SIGMA_ALLOW_MIN, SIGMA_ALLOW_MAX
)

def validate_float_input(value_str: str, min_val: float, max_val: float) -> float:
    try:
        val = float(value_str)
    except ValueError:
        raise ValueError("Ошибка: Введенное значение должно быть числом.")
    
    if not (min_val <= val <= max_val):
        raise ValueError(f"Ошибка: Значение вышло за диапазон [{min_val} .. {max_val}].")
    
    return val

def get_valid_dimension(prompt: str) -> float:
    while True:
        try:
            user_input = input(prompt)
            return validate_float_input(user_input, DIMENSION_MIN, DIMENSION_MAX)
        except ValueError as e:
            print(e)

def get_valid_moment(prompt: str) -> float:
    while True:
        try:
            user_input = input(prompt)
            return validate_float_input(user_input, MOMENT_MIN, MOMENT_MAX)
        except ValueError as e:
            print(e)

def get_valid_sigma(prompt: str) -> float:
    while True:
        try:
            user_input = input(prompt)
            return validate_float_input(user_input, SIGMA_ALLOW_MIN, SIGMA_ALLOW_MAX)
        except ValueError as e:
            print(e)
