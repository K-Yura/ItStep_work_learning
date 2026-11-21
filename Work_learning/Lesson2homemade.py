num1 = int(input("перше число: "))
num2 = int(input("друге число: "))
sum = num1 + num2
average = float(sum / 2)
print("Сума:", sum)
print("Середнє:", average)
# Helper
num1 = float(input("Перше число: "))
num2 = float(input("Друге число: "))
sum_result = num1 + num2
average = sum_result / 2
print("Сума:", sum_result)
print("Середнє арифметичне:", average)

sum = float(input("ВВЕДІТЬ ВАШУ СУМУ, грн.: "))
usd = float(input("ВВЕДІТЬ КУРС ВАЛЮТИ: "))
exchange = round((sum / usd), 2)
print("ДО ВИДАЧІ ВАЛЮТИ:", exchange)

price = float(input("ВВЕДІТЬ ВАРТІСТЬ ТОВАРУ: "))
perc = int(input("ВВЕДІТЬ ВІДСОТОК ЗНИЖКИ: "))
discount = round((price * perc / 100), 2)
print("СУМА ВАШОЇ ЗНИЖКИ:", discount)

print("**********ВАША ВИТРАТА КАЛОРІЙ**********")
print("РЕЖИМИ ВАШОГО ДЕННОГО НАВАНТАЖЕННЯ")
sl_walk = float(input("ПОВІЛЬНА ХОДЬБА, хв.: "))
br_walk = float(input("ШВИДКА ХОДЬБА, хв.: "))
ea_run = float(input("ЛЕГКИЙ БІГ, хв.: "))
calories1 = sl_walk * 3
calories2 = br_walk * 4.5
calories3 = ea_run * 9
calories = round((calories1 + calories2 + calories3), 3)
print("ДЕННА ВИТРАТА ВАМИ КІЛОКАЛОРІЙ СКЛАДАЄ:", calories)
