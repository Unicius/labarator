f = True

try:
    n = int(input("Введите количество элементов в массиве: "))
    if f:
        if n <= 0:
            f = False
            error = "Число меньше или равно нулю"
    array = []
    print(f"Введите {n} действительных чисел (каждое с новой строки):")
    while len(array) < n:
        try:
            element = float(input(f"Элемент {len(array) + 1}: "))
            array.append(element)
        except ValueError:
            f = False
            error = "Ошибка: Неверный формат числа! Используйте точку для дробной части (например, 5.5). Попробуйте снова."
    
    print("Исходный массив:", array)
    total_sum = sum(array)
    average = total_sum / n
    print(f"Среднее арифметическое всех элементов: {average:.4f}")
    for i in range(n):
        if array[i] == 0:
            array[i] = average
            # print("Измененный массив:", array)
            f = False

except ValueError:
    f = False
    error = "Ошибка: неверный формат данных"
if f:
    print("Измененный массив:", array)

else:
    print(error)