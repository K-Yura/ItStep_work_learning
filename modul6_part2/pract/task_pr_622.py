# Користувач вводить рядок та два індекси. Виведіть
# зріз рядка. Виправіть помилку в коді
# text = input("Введіть рядок: ")
#
# start = float(input("Введіть початковий індекс: "))
# end = float(input("Введіть кінцевий індекс: "))
#
# segment = text[start, end]
#
# print(segment)

text = input("Введіть рядок: ")

start = int(input("Введіть початковий індекс: "))
end = int(input("Введіть кінцевий індекс: "))

segment = text[start:end]

print(segment)
