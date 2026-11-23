text = input("Введіть текст: ")

letters = 0
digits = 0

for symbol in text:
    if symbol.isalpha():
        letters += 1
    elif symbol.isdigit():
        digits += 1

print(f"Кількість літер: {letters}")
print(f"Кількість цифр: {digits}")
