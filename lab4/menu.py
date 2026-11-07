from constants import SECTION_RECTANGULAR, SECTION_ROUND, SECTION_I_BEAM

def show_menu() -> None:
    """Выводит стартовое меню выбора типа сечения балки."""
    print("\n" + "="*50)
    print("Вариант 8. Прочность балки на изгиб")
    print("="*50)
    print("Выберите тип сечения балки:")
    print("1 — Прямоугольное (W = b * h² / 6)")
    print("2 — Круглое (W = π * d³ / 32)")
    print("3 — Двутавр (для упрощения W = h³ / 12)")
    print("0 — Выход из программы")
    print("="*50)

def route_menu(choice: str) -> int | None:
    """Маршрутизация выбора пользователя через match-case конструкцию."""
    match choice:
        case "1":
            return SECTION_RECTANGULAR
        case "2":
            return SECTION_ROUND
        case "3":
            return SECTION_I_BEAM
        case "0":
            return None
        case _:
            print("Ошибка: Неверный пункт меню. Попробуйте снова.")
            return -1
