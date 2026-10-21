import math

success = True
error_msg = ""
result_msg = ""

try:
    choice = int(input("Выберите тип сечения (1 — прямоугольное, 2 — круглое, 3 — двутавр): "))
except ValueError:
    success = False
    error_msg = "Ошибка: неверный формат."

W = 0.0
shape_type = ""

if success:
    match choice:
        case 1:
            shape_type = "прямоугольное"
            try:
                b = float(input("Введите ширину b (мм, от 10 до 1000): "))
                h = float(input("Введите высоту h (мм, от 10 до 1000): "))
                if not (10 <= b <= 1000 and 10 <= h <= 1000):
                    success = False
                    error_msg = "Ошибка: размеры сечения выходят за диапазон 10..1000 мм."
                else:
                    W = (b * (h ** 2)) / 6
            except ValueError:
                success = False
                error_msg = "Ошибка: неверный формат ввода размеров сечения."
        case 2:
            shape_type = "круглое"
            try:
                d = float(input("Введите диаметр d (мм, от 10 до 1000): "))
                if not (10 <= d <= 1000):
                    success = False
                    error_msg = "Ошибка: диаметр выходит за диапазон 10..1000 мм."
                else:
                    W = (math.pi * (d ** 3)) / 32
            except ValueError:
                success = False
                error_msg = "Ошибка: неверный формат ввода диаметра."
        case 3:
            shape_type = "двутавр"
            try:
                h = float(input("Введите высоту h (мм, от 10 до 1000): "))
                if not (10 <= h <= 1000):
                    success = False
                    error_msg = "Ошибка: высота двутавра выходит за диапазон 10..1000 мм."
                else:
                    W = (h ** 3) / 12
            except ValueError:
                success = False
                error_msg = "Ошибка: неверный формат ввода высоты."
        case _:
            success = False
            error_msg = "Ошибка: выбран несуществующий пункт меню."

if success:
    try:
        M = float(input("Введите изгибающий момент M (кН·м, от 0.1 до 500): "))
        omega_allow = float(input("Введите допускаемое напряжение omega (МПа, от 50 до 400): "))
        
        if not (0.1 <= M <= 500):
            success = False
            error_msg = "Ошибка: изгибающий момент выходит за границы (0.1..500 кН·м)."
        elif not (50 <= omega_allow <= 400):
            success = False
            error_msg = "Ошибка: допускаемое напряжение выходит за границы (50..400 МПа)."
        else:
            omega = (M * 1_000_000) / W
            k_use = omega / omega_allow
            
            if k_use < 0.5:
                Class = "большой запас"
            elif 0.5 <= k_use <= 1.0:
                Class = "допустимо"
            else:
                Class = "перегрузка"
                
            result_msg = (
                f"--- Вывод результатов ---\n"
                f"Тип сечения: {shape_type}\n"
                f"Момент сопротивления W: {W:.2f} мм³\n"
                f"Напряжение σ: {omega:.2f} МПа\n"
                f"Коэффициент использования (σ/[σ]): {k_use:.4f}\n"
                f"Класс: {Class}"
            )
    except ValueError:
        success = False
        error_msg = "Ошибка: неверный формат ввода числовых данных M или [σ]."

if success:
    print(result_msg)
else:
    print(error_msg)
