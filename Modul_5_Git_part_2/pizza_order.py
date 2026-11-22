print("\nЗАМОВЛЕННЯ ПІЦИ")
print("*" * 35)

pizzas_1 = "Маргарита"
pizzas_2 = "Пепероні"
pizzas_3 = "Чотири сири"

price_pizzas_1 = 150
price_pizzas_2 = 180
price_pizzas_3 = 200

while True:
    print("МЕНЮ")
    print("1. Вибрати піцу")
    print("2. Вихід")
    print("*" * 35)

    choice = input("\nВаш вибір: ")

    if choice == "1":
        print("\nМеню піц:")
        print(f"{pizzas_1} - {price_pizzas_1} грн")
        print(f"{pizzas_2} - {price_pizzas_2} грн")
        print(f"{pizzas_3} - {price_pizzas_3} грн")
        print("*" * 35)

        pizza = input("\nВведіть назву піци: ").strip().lower()

        if pizza == pizzas_1.lower():
            pizza = pizzas_1
        elif pizza == pizzas_2.lower():
            pizza = pizzas_2
        elif pizza == pizzas_3.lower():
            pizza = pizzas_3
        else:
            print("ПОМИЛКА! Такої піци в Меню не існує.")
            continue

        quantity = int(input("\nВведіть кількість: "))
        print(f'Замовлена піца "{pizza}", в кількості {quantity} шт.')

    elif choice == "2":
        print("*" * 35)
        print("До зустрічі наступного разу!")
        break

    else:
        print("*" * 35)
        print("ПОМИЛКА! Невірний вибір! Спробуйте ще раз.")
