items = input("Введіть ваші речі: ")

items = items.lower()

if "ніж" in items or "гроші" in items or "отрута" in items:
    print("У вас є речі які заборонено перевозити")
else:
    print("Оформлено доставку")
