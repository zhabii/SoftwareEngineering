#9 вывести, четное или нечетное число ввел пользователь
usrNum = int(input("введите свое число: "))
answer = "четное" if usrNum % 2 == 0  else "нечетное"
print(f"число {usrNum} - {answer}")


#вывод текущей даты
from datetime import date
today = date.today()
print("Текущая дата : ", today)