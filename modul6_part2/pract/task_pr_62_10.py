# Користувач вводить математичний вираз, наприклад
# 23+45. Виведіть результат
# Обробіть такі математичні операції – +*/-
# Реалізуйте як консольну програму(закінчити якщо
# введено EXIT)

while True:
    expression = input("Введіть вираз або EXIT для виходу: ")

    if expression.upper() == "EXIT":
        print("Програму завершено.")
        break

    result = 0
    symbol = ""
    index = 0

    for i in range(len(expression)):
        if expression[i] in "+-*/":
            symbol = expression[i]
            index = i
            break

    if not symbol:
        print("Невірний вираз!")
        continue

    first_number = float(expression[:index])
    second_number = float(expression[index + 1 :])

    if symbol == "+":
        result = first_number + second_number
    elif symbol == "-":
        result = first_number - second_number
    elif symbol == "*":
        result = first_number * second_number
    elif symbol == "/":
        if second_number == 0:
            print("Помилка: ділення на нуль!")
            continue
        result = first_number / second_number

    print(f"Результат: {result:.3}")
