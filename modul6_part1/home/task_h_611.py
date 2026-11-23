# Завдання 1
# Користувач вводить рядок англійською мовою. Порахуйте
# скільки в ньому голосних літер(aeuio)
# Виправіть помилки в коді
# text = input("Введіть рядок англійською мовою: ")
#
# count = 0
# for letter in text:
#     if "aeiou" in letter:
#         count += 1
#
# print(f"Кількість голосних літер: {count}")

text = input("Введіть рядок англійською мовою: ").lower()

count = 0

for letter in text:
    if letter in "aeiou":
        count += 1

print(f"Кількість голосних літер: {count}")
