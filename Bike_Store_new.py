# --- байки, запчасти
# запчасти: рама, руль, цепь, педали, скорости
# каждой части должно быть минимум по 3 бренда с разными ценами (примерно 60-120 за целый байк)
# если деталь одного бренда заканчивается, её надо до-заказать.

import random
from random import choice, randrange


class Pay_System:
    def order(self, order):
        print('Заказ')
        print('===================')
        print(f' Деталь: {order.part} - Бренд: {order.brand}')
        print(f' Стоимость: {order.cost()}')
        print(f' Закончились детали:')
        print(f' Деталь: {order.out_of_part()} - Бренд: {order.out_of_brand()}')


class Order():
    def __init__(self, part, brand):
        self.part = part
        self.brand = brand


class Parts_Brand_Cost(Order):
    def __init__(self, part, brand, types_parts, types_price, types_brand, prices_brand):
        super().__init__(part, brand)
        self.types = types_parts
        self.price = types_price
        self.name = types_brand
        self.kof = prices_brand

    def cost(self):
        x = self.types.index(part)
        price_part = self.price[x]
        y = self.name.index(brand)
        price_brand = self.kof[y]
        cost = price_part * price_brand
        return cost

    def out_of_part(self):
        z = choice(self.types)
        return z

    def out_of_brand(self):
        q = choice(self.name)
        return q


types_parts = ['frame', 'handlebar', 'chain', 'pedals', 'shifters']
types_price = [7, 8, 9, 10, 12]
types_brand = ['Trek', 'GT', 'LTD']
prices_brand = (1.3, 1.8, 2)
print('введите название запчасти ''frame', 'handlebar', 'chain', 'pedals', 'shifters')
part = input()
print('введите бренд ''Trek', 'GT', 'LTD')
brand = input()
pokupka = Parts_Brand_Cost(part, brand, types_parts, types_price, types_brand, prices_brand)
pay_system = Pay_System()
pay_system.order(pokupka)

