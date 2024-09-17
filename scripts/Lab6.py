#math operations
def math_opetarions(a, b):
    print(f"{a} в степени {b} =", a ** b)
    print(f"{a} делить на {b} =", a / b)
    print(f"{a} целочисленно разделить на {b} =", a // b)
    print(f"остаток от деления {a} на {b} =", a % b)
    print("______________________________________________")

#int
a, b = 7, 5
math_opetarions(a, b)
#float
a, b = 6.3, 3.2
math_opetarions(a, b)
#int & float
a, b = 8, 2.9
math_opetarions(a, b)


#вывод текущей даты
from datetime import date
today = date.today()
print("Текущая дата : ", today)