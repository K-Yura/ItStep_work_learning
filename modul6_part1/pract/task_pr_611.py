text = input("Введіть рядок: ")
symbol = input("Введіть символ: ")

count_symbol = text.count(symbol)

print(f"Символ '{symbol}' зустрічається {count_symbol} раз(и)")

text = input("Введіть рядок: ")
symbol = input("Введіть символ: ")

count_symbol = 0

for ch in text:
    if ch == symbol:
        count_symbol += 1

print(f"Символ '{symbol}' зустрічається {count_symbol} раз(и)")
