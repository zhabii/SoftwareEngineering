#в python работает динамическая типизация!
number = 5
clock = 3.14
book = "Hello World!"
boolean = True

#type()
print(type(number))
print(type(clock))
print(type(book))
print(type(boolean))

#print() and vars
print("age : ", number)
print(number, clock, book)

#приведение типов
print("число pi примерно равно " + str(clock))



#вывод текущей даты
from datetime import date
today = date.today()
print("Текущая дата : ", today)