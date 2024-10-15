#кортежи - константные списки
my_tuple = (1, 2, 3)
another_tuple = 4, 5, 6 #python автоматически создаст кортеж

#кортежи используются в функциях для принятия и возврата нескольких значений
def my_function():
    return 1, 2, 3

new_tuple = my_function()
print(my_tuple, type(my_tuple))
a, b, c = my_tuple
print(a, b, c, sep="---")