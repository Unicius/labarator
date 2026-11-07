"""Точка входа. Запуск расчёта."""

import menu


def main():
    menu.display_main_menu()
    user_choice = input("Выберите пункт: ").strip()
    menu.handle_choice(user_choice)


if __name__ == "__main__":
    main()