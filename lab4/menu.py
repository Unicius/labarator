"""Модуль отображения меню и маршрутизации (match-case)."""

from validators import validate_float_input
from constants import (
    SECTION_DIM_MIN, SECTION_DIM_MAX,
    MOMENT_MIN, MOMENT_MAX,
    ALLOWABLE_STRESS_MIN, ALLOWABLE_STRESS_MAX,
    SECTION_TYPES
)
import operations


def display_main_menu():
    print("\n" + "=" * 45)
    print("      РАСЧЁТ ПРОЧНОСТИ БАЛКИ НА ИЗГИБ      ")
    print("=" * 45)
    print(" Выберите тип поперечного сечения балки:")
    print(" 1 — Прямоугольное (W = b · h² / 6)")
    print(" 2 — Круглое (W = π · d³ / 32)")
    print(" 3 — Двутавр (упрощённо W = h³ / 12)")
    print(" 0 — Выход из программы")
    print("-" * 45)


def handle_choice(choice: str) -> bool:
    """Маршрутизация выбора пользователя через match-case. Возвращает False при выходе."""
    match choice:
        case "1":
            section_type = SECTION_TYPES["1"]
            b = validate_float_input("Введите ширину b (мм, 10..1000): ", SECTION_DIM_MIN, SECTION_DIM_MAX)
            h = validate_float_input("Введите высоту h (мм, 10..1000): ", SECTION_DIM_MIN, SECTION_DIM_MAX)
            w = operations.calculate_w_rectangle(b, h)
            _process_calculation(section_type, w)

        case "2":
            section_type = SECTION_TYPES["2"]
            d = validate_float_input("Введите диаметр d (мм, 10..1000): ", SECTION_DIM_MIN, SECTION_DIM_MAX)
            w = operations.calculate_w_circle(d)
            _process_calculation(section_type, w)

        case "3":
            section_type = SECTION_TYPES["3"]
            h = validate_float_input("Введите высоту h (мм, 10..1000): ", SECTION_DIM_MIN, SECTION_DIM_MAX)
            w = operations.calculate_w_i_beam(h)
            _process_calculation(section_type, w)

        case "0":
            print("Завершение работы программы...")
            return False

        case _:
            print("Ошибка: неверный пункт меню. Попробуйте снова.")

    return True


def _process_calculation(section_type: str, w: float):
    """Сбор общих параметров и вывод итогового результата."""
    moment = validate_float_input("Введите изгибающий момент M (кН·м, 0.1..500): ", MOMENT_MIN, MOMENT_MAX)
    allowable = validate_float_input("Введите допускаемое напряжение [σ] (МПа, 50..400): ", ALLOWABLE_STRESS_MIN, ALLOWABLE_STRESS_MAX)

    sigma, utilization, status_class = operations.calculate_stress_and_status(w, moment, allowable)

    print("\n" + "-" * 35)
    print("РЕЗУЛЬТАТЫ РАСЧЁТА:")
    print(f"Тип сечения: {section_type}")
    print(f"Момент сопротивления W: {w:.2f} мм³")
    print(f"Напряжение σ: {sigma:.2f} МПа")
    print(f"Допускаемое [σ]: {allowable:.2f} МПа")
    print(f"Коэффициент использования (σ/[σ]): {utilization:.4f}")
    print(f"Класс прочности: {status_class}")
    print("-" * 35)