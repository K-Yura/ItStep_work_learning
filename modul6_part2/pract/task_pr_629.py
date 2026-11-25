# Завдання 9
# Користувач вводить слова поки не введе слово END.
# Збережіть це слово до одного з 4-ох рядків:
# ● герундій – закінчується на ing
# ● дієслово past tense – закінчується на ed
# ● починаються на голосну – aeuio
# ● решта
# Слова можуть вводитися як великими так і малими літерами

gerund = ""
past_tense = ""
vowels = ""
other = ""

while True:
    word = input("Введіть слово: ")

    if word.upper() == "END":
        break

    word = word.lower()

    if word[-3:] == "ing":
        gerund += word + ", "
    elif word[-2:] == "ed":
        past_tense += word + ", "
    elif word[0] in "aeiou":
        vowels += word + ", "
    else:
        other += word + ", "

print("Герундій:", gerund[:-2])
print("Past Tense:", past_tense[:-2])
print("Починаються на голосну:", vowels[:-2])
print("Решта:", other[:-2])
