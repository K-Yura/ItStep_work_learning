# Завдання 3
# Користувач вводить текст. Порахуйте скільки в ньому речень

text = input("Введіть текст: ")

sentence = 0

for symbol in text:
    if symbol in ".!?":
        sentence += 1

print(f"Кількість речень в тексті: {sentence}")
