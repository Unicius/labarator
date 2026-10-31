nums = input("Введите числа через пробел: ")

try:
    numbers = [float(x) for x in nums.split()]
    if not numbers:
        raise ValueError("Вы не ввели ни одного числа.")
    
    total_sum = sum(numbers)
    total_umnoj = 1
    for num in numbers:
        total_umnoj *= num

    print(f"Сумма элементов: {total_sum}")
    print(f"Произведение элементов: {total_umnoj}")

except ValueError:
    print(f"Ошибка ввода: Неверный формат данных! Подробности")
