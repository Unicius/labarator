text = input("Введите строку: ").strip()
if not text:
    print("Ошибка: строка не должна быть пустой.")

elif not text.endswith('.'):
    print("Ошибка: строка должна заканчиваться точкой.")

elif text.count('.') > 1:
    print("Ошибка: в строке может быть только одна точка (в конце).")

elif any(char.isdigit() for char in text):
    print("Ошибка: ввод чисел запрещен.")

else:
    cleaned_text = text[:-1].strip()
    word_count = len(cleaned_text.split())
    print(f"Количество слов в строке: {word_count}")
