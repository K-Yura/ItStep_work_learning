text = input("Введіть рядок: ")

print(f"Кількість символів: {len(text)}")

if "python" in text.lower():
    print('Слово "python" є в рядку')
else:
    print('Слова "python" немає в рядку')

count_hushing = 0

for ch in text.lower():
    if ch in "szh":
        count_hushing += 1

print(f"Кількість шиплячих літер: {count_hushing}")
