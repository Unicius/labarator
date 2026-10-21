from math import *
print("Расчёт балки на изгиб")
print("1 — Прямоугольное сечение")
print("2 — Круглое сечение")
print("3 — Двутавр (упрощённо)")
try:
    shape_type = int(input("Выбирите тип сечения 1, 2 или 3:"))
    if shape_type < 1 or shape_type > 3:
        print("Нет такого выбора!")
        exit()
except ValueError:
    print("Вы ввели недопустимые значения")
    exit()
min_size, max_size = 10.0, 1000.0


match shape_type:
    case 1:
        name = "Прямоугольное"
        b = float(input("Введите ширину (мм, 10..1000): "))
        h = float(input("Введите высоту (мм, 10..1000): "))
        if not (min_size <= b <= max_size):
                print(f"Ошибка: ширина выходит за диапазон {min_size}..{min_size} мм.")
                exit()
        W = (b*h**2) / 6
    
    case 2:
        name = "Круглое"
        d = float(input("Введите диаметр (мм, 10..1000): "))
        if not (min_size <= d <= max_size):
                        print(f"Ошибка: ширина выходит за диапазон {min_size}..{min_size} мм.")
                        exit()
        W = (pi*d**3) / 32
    
    case 3:
        name = "Двутавр"
        h = float(input("Введите высоту (мм, 10..1000): "))
        if not (min_size <= h <= max_size):
                        print(f"Ошибка: ширина выходит за диапазон {min_size}..{min_size} мм.")
                        exit()
        W = h**3 / 12
    
    case _:
        print("Ошибка неверный выбор типа сечения")
        exit()

try:
    M = float(input("Введите изгибающий момент (кН·м, 0.1..500): "))
    if not (0.1 <= M <= 500.0):
        print("Ошибка: момент M должен быть в диапазоне от 0.1 до 500.0 кН·м.")
        exit()

except ValueError:
       print("Вы ввели недопустимые значения")
       exit()

try:
    omega = float(input("Введите допускаемое напряжение (МПа, 50...400)"))
    if not (50.0 <= omega <= 400.0):
          print("Ошибка: момент omega должен быть в диапазоне от 50 до 400 кН·м.")
          exit()
except ValueError:
    print("Вы ввели недопустимые значения")
    exit()

omeg = (M*1000)/(W*1000)
k = omeg / omega
match k:
    case _ if k < 0.5:
        Class = "большой запас"
    case _ if 0.5 <= k <= 1.0:
        Class = "допустимо"
    case _:
        Class = "перегрузка"

print("Результаты расчёта")
print(f"Тип сечения: {shape_type}")
print(f"Момент сопротивления W: {W:.2f} мм³")
print(f"Расчетное напряжение omega: {omeg:.2f} МПа")
print(f"Допускаемое напряжение [omega]: {omega:.2f} МПа")
print(f"Коэффициент использования (omega/[omega]): {k:.3f}")
print(f"Класс: {Class}")