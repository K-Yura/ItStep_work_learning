# Завдання 2
# Користувач вводить текст.
# Після чого запускається цикл і користувач вводить певне
# слово. Треба це слово в тексті замінити на верхній регістр.
# Цикл закінчується коли введено EXIT
# Приклад:
# Текст – a big red fox is eating red apple
# Слово red – a big RED fox is eating RED apple
# Слово fox – a big RED FOX is eating RED apple
# Слово EXIT – кінець програми, показати результат

text = input("Введіть текст: ")

while True:
    word = input("Введіть слово (або EXIT для завершення та виведення результату): ")

    if word == "EXIT":
        break

    text = text.replace(word, word.upper())
    print(text)

print("Результат зміни регістру:")
print(text)
