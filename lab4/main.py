from menu import show_menu, route_menu
import validators
import operations
from constants import SECTION_NAMES

def main():
    while True:
        show_menu()
        user_choice = input("Введите ваш выбор: ").strip()
        
        # Маршрутизация через match-case
        section_type = route_menu(user_choice)
        
        if section_type is None:
            print("Завершение работы программы")
            break
        if section_type == -1:
            continue
            
        print(f"\nВыбран тип сечения: {SECTION_NAMES[section_type]}")
        
        # Безопасный ввод параметров с валидацией границ
        size = validators.get_valid_dimension("Введите характерный размер сечения (мм, от 10 до 1000): ")
        moment = validators.get_valid_moment("Введите изгибающий момент M (кН·м, от 0.1 до 500): ")
        sigma_allow = validators.get_valid_sigma("Введите допускаемое напряжение [σ] (МПа, от 50 до 400): ")
        
        # Вычисления
        w = operations.calculate_w(section_type, size)
        sigma = operations.calculate_sigma(moment, w)
        k_use, safety_class = operations.classify_usage(sigma, sigma_allow)
        
        # Вывод результатов
        print("\n" + "-"*40)
        print("РЕЗУЛЬТАТЫ РАСЧЕТА:")
        print(f"Тип сечения:           {SECTION_NAMES[section_type]}")
        print(f"Момент сопротивления W: {w:.2f} мм³")
        print(f"Расчетное напряжение σ: {sigma:.2f} МПа")
        print(f"Допускаемое [σ]:       {sigma_allow:.2f} МПа")
        print(f"Коэф. использования:    {k_use:.4f}")
        print(f"Класс состояния:       {safety_class.upper()}")
        print("-"*40)
        
        # Возможность выполнить несколько расчетов подряд
        again = input("Хотите выполнить еще один расчет? (д/н, yes/no, y/n): ").strip().lower()
        if again not in ['д', 'y', 'yes', 'да']:
            print("Завершение работы программы.")
            break

if __name__ == "__main__":
    main()
