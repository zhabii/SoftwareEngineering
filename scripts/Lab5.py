
var1 = str(input("type string: "))
var2 = int(input("type integer number: "))
var3 = float(input("type float number: "))

print("values of variables: ")
print(var1, var2, var3, sep="\n")

#вывод текущей даты
from datetime import date
today = date.today()
print("Текущая дата : ", today)