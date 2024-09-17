name = "Артём"
age = 20
print(f"Меня зовут {name}, мне {age} лет")

x, y = 13, 21
print(f"сумма {x} и {y} равна {x + y}")

a, b = 1, 5
print(f"между {a} и {b} стоит {list(range(a+1, b))}")

#вывод текущей даты
from datetime import date
today = date.today()
print("Текущая дата : ", today)