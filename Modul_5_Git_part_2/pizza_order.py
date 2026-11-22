print("\nЗАМОВЛЕННЯ ПІЦИ")
print("*" * 35)

while True:
    print("\nМЕНЮ")
    print("1. Вибрати піцу")
    print("2. Вихід")
    print("*" * 35)

    choice = input("\nВаш вибір: ")

    if choice == "1":
        pizza = input("Введіть назву піци: ")
        quantity = int(input("Введіть кількість: "))
        print(f'Замовлена піца "{pizza}", в кількості {quantity} шт.')

    elif choice == "2":
        print("*" * 35)
        print("До зустрічі наступного разу!")
        break

    else:
        print("*" * 35)
        print("ПОМИЛКА! Невірний вибір! Спробуйте ще раз.")
