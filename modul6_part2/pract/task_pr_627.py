# Завдання 7
# Користувач вводить рядок та символ. Виведіть індекс
# цього символу.

text = input("Введіть рядок: ")
symbol = input("Введіть символ: ")

for i in range(len(text)):
    if text[i] == symbol:
        print(f'Індекс символу "{symbol}"- {i}')
        break
else:
    print("Символ не знайдено")
