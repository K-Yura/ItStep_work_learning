# Завдання 2
# Користувач вводить числа, поки не введе -1.
# Збережіть усі ці числа в список. Виведіть їхню кількість,
# суму, мінімальне, максимальне та середнє.
# Скористайтесь функціями min, max, sum, len

numbers = []

while True:
    num = int(input("Введіть число (Для завершення потрібно ввести: -1): "))

    if num == -1:
        break

    numbers.append(num)

print("Кількість чисел:", len(numbers))
print("Сума чисел:", sum(numbers))
print("Мінімальне число:", min(numbers))
print("Максимальне число:", max(numbers))
print(f"Середнє: {sum(numbers) / len(numbers):.3f}")
