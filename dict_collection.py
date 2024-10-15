#dictonary comprehension
my_dict = {x: x**2 for x in range(1, 5)}
print(my_dict)

#fromkeys - создает словарь по списку ключей и присваивает всем одно значение
keys = ['apple', 'banana', 'cherry']
my_dict = dict.fromkeys(keys, 22)
print(my_dict)

#OrderedDict - сохраняет порядок элементов
from collections import OrderedDict

my_ordered_dict = OrderedDict()
my_ordered_dict['apple'] = 1
my_ordered_dict['banana'] = 2
my_ordered_dict['cherry'] = 3
print(my_ordered_dict)

#методы
print(my_dict.keys())   #все ключи
print(my_dict.values()) #все значения
print(my_dict.items())  #пары ключ-значение (через кортеж)


print(my_dict.get('apple'))  #дает значение по ключу
print(my_dict.get('mango', 'default_value')) #если элемент не найден, возвращает 'default_value'

#pop и popitem

my_dict = {'apple': 1, 'banana': 2}
other_dict = {'cherry': 3, 'date': 4}
my_dict.update(other_dict) #словарь other_dict добавился к словарю my_dict
print(my_dict)



