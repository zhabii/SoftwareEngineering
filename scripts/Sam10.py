#10 пользователь вводит три строки str, каждая из них выводится n раз, где n - len(str)
str1, str2, str3 = str(input("str1: ")), str(input("str2: ")), str(input("str3: "))
print(str1 * len(str1))
print(str2 * len(str2))
print(str3 * len(str3))

#вывод текущей даты
from datetime import date
today = date.today()
print("Текущая дата : ", today)