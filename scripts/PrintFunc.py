print("Два плюс два равно 4")
print("Два плюс два равно", 4, 5, 6)

#sep
print(1, 2, 3)
print(1, 2, 3, sep=',')
print(1, 2, 3, sep=',', end='.\t')
print("-> this is next line")

#вывод текущей даты
from datetime import date
today = date.today()
print("Текущая дата : ", today)
