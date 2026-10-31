# N1 2)
f = True
count = 0
dig_sum = 0
try:
    N = int(input("Введите любое число: "))


    if f:
        if N <= 0:
            f = False
            error = "Число меньше 0, введите число большее 0"

    while N > 0:
        last_dig = N % 10
        dig_sum += last_dig
        count += 1
        N //= 10

except ValueError:
    f = False
    error = "Вы ввели неверный формат ввода"
if f:
    print(f"Количество цифр {count}")
    print(f"Сумма цифр {dig_sum}")
else:
    print(error)
