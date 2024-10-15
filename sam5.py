"""
Есть магазин, который продает разные товары.
Для каждого товара хранятся его название, количество на складе и цена
в виде списка кортежей, где каждый кортеж содержит данные о товаре (название, количество, цена)

Написать программу, которая
1. выводит на экран все товары с их количеством и ценой.
2. рассчитывает общую стоимость всех товаров в магазине

"""

inventory = [
    ('apples', 50, 1.20),
    ('bananas', 30, 0.50),
    ('oranges', 20, 0.80),
    ('grapes', 40, 2.50),
]


def display_inventory(inventory):
    print("Текущий инвентарь магазина:")
    total_value = 0
    for item in inventory:
        name, count, price = item
        total_value += count * price
        print(f"Товар: {name}, Количество: {count}, Цена: ${price:.2f}")
    print(f"Общая стоимость всех товаров на складе: ${total_value:.2f}")


display_inventory(inventory)