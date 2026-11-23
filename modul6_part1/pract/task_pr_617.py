# Користувач вводить пароль поки не введе його правильно.
# Правильний пароль повинен:
# ● Бути довшим за 8 символів
# ● Містити хоча б одну цифру
# ● Містити хоча б одну літеру

while True:
    password = input("Введіть пароль: ")

    is_letter = False
    is_digit = False

    for symbol in password:
        if symbol.isalpha():
            is_letter = True
        if symbol.isdigit():
            is_digit = True

    if len(password) > 8 and is_letter and is_digit:
        print("Пароль прийнято")
        break
