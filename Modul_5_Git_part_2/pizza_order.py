print("\nЗАМОВЛЕННЯ ПІЦИ")
print("=" * 50)

pizzas_1 = "Маргарита"
pizzas_2 = "Пепероні"
pizzas_3 = "Чотири сири"

price_pizzas_1 = 150
price_pizzas_2 = 180
price_pizzas_3 = 200

order_pizza_1 = 0
order_pizza_2 = 0
order_pizza_3 = 0

while True:
    print("\nМЕНЮ ДІЙ:")
    print("1. Показати меню ресторану")
    print("2. Вибрати піцу")
    print("3. Показати замовлення")
    print("4. Вихід")
    print("=" * 50)

    choice = input("\nВаша дія: ")
    print("=" * 50)

    if choice == "1":
        print("\nМЕНЮ РЕСТОРАНУ:")
        print("=" * 50)
        print(f"{pizzas_1} - {price_pizzas_1} грн")
        print(f"{pizzas_2} - {price_pizzas_2} грн")
        print(f"{pizzas_3} - {price_pizzas_3} грн")
        print("=" * 50)

    elif choice == "2":
        pizza = input("\nВведіть назву піци: ").strip().lower()
        print("=" * 50)

        if pizza == pizzas_1.lower():
            pizza = pizzas_1
        elif pizza == pizzas_2.lower():
            pizza = pizzas_2
        elif pizza == pizzas_3.lower():
            pizza = pizzas_3
        else:
            print("=" * 50)
            print("ПОМИЛКА! Такої піци в Меню ресторану не існує.")
            print("=" * 50)
            continue

        quantity = int(input("\nВведіть кількість: "))

        if quantity <= 0:
            print("=" * 50)
            print("ПОМИЛКА! Кількість піц повинна бути більшою за 0.")
            print("=" * 50)
            continue

        total_pizzas = order_pizza_1 + order_pizza_2 + order_pizza_3

        if total_pizzas + quantity > 15:
            print("=" * 50)
            print("ПОМИЛКА! Загальна кількість піц не може бути більшою за 15.")
            print("=" * 50)
            continue

        if pizza == pizzas_1:
            order_pizza_1 += quantity
        elif pizza == pizzas_2:
            order_pizza_2 += quantity
        elif pizza == pizzas_3:
            order_pizza_3 += quantity

        print(f'Замовлена піца "{pizza}", в кількості {quantity} шт.')
        print("=" * 50)

    elif choice == "3":
        cost_1 = order_pizza_1 * price_pizzas_1
        cost_2 = order_pizza_2 * price_pizzas_2
        cost_3 = order_pizza_3 * price_pizzas_3

        total_cost = cost_1 + cost_2 + cost_3
        if total_cost == 0:
            print("=" * 50)
            print("ЗАМОВЛЕННЯ ЩЕ НЕ ЗРОБЛЕНЕ! Зробіть замовлення.")
            print("=" * 50)
            continue

        print("ВАШЕ ЗАМОВЛЕННЯ")
        print("=" * 50)
        print("Піца\t\tКількість\tВартість")
        print("-" * 50)

        if order_pizza_1 > 0:
            print(f"{pizzas_1}\t\t{order_pizza_1}\t\t{cost_1} грн")

        if order_pizza_2 > 0:
            print(f"{pizzas_2}\t\t{order_pizza_2}\t\t{cost_2} грн")

        if order_pizza_3 > 0:
            print(f"{pizzas_3}\t\t{order_pizza_3}\t\t{cost_3} грн")

        print("-" * 50)
        print(f"Загальна вартість: {total_cost} грн")
        print("=" * 50)
        print("Дякуємо за замовлення!")

    elif choice == "4":
        print("=" * 50)
        print("До зустрічі наступного разу!")
        break

    else:
        print("=" * 50)
        print("ПОМИЛКА! Невірний вибір! Спробуйте ще раз.")
        print("=" * 50)
