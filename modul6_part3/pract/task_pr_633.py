# Завдання 3
# Користувач вводить числа, поки не введе 0. Створіть
# два нових списки: з додатніми та від’ємними числами.
# Виведіть елементи обох списків на екран.
# Виправіть помилку в коді
# while True:
#     number = int(input("Введіть число (0 для завершення): "))
#
#     positive = []
#     negative = []
#
#     if number < 0:
#         positive.append(number)
#     else:
#         negative.append(number)
#
# print("Додатні числа:", positive)
# print("Від'ємні числа:", negative)

positive = []
negative = []

while True:
    number = int(input("Введіть число (0 для завершення): "))

    if number == 0:
        break

    if number > 0:
        positive.append(number)
    else:
        negative.append(number)

print("Додатні числа:", positive)
print("Від'ємні числа:", negative)
