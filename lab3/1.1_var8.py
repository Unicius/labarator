# Вариант 8
# N1 1)
f = True
sum_odds = 0
still_odd = 1
try:
    chet = int(input("Введите количество чисел n: "))
    if f:
        if chet <= 0:
            f = False
            error = "Число меньше или равно нулю"

    print(f"Введите {chet} вещественных чисел (каждое с новой строки):")
            
    for _ in range(chet):
        x = float(input())
        is_odd = int(int(x) % 2 != 0)
        still_odd *= is_odd
        sum_odds += x * still_odd

except ValueError:
    f = False
    error = ("Неверный формат")

if f:
    print(f"Сумма нечет чисел {sum_odds}")
else:
    print(error)