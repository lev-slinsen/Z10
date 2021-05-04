# --- клиенты, чеки, покупки
# время покупки
# список товаров

'''
дата: 01.30.2022
время покупки: 12.30
список товаров: объекты
сумма: 420
сумма со скидкой: 69
'''
from datetime import date
import random


class CalendarTimer():
    def __init__(self):
        self.start_date = date.today().replace(day=1, month=1).toordinal()
        self.end_date = date.today().toordinal()
        self.random_day = date.fromordinal(random.randint(self.start_date, self.end_date)) #искомая рандомная дата
        hours = random.randrange(12, 20) #c 12 до 8 то биш с 12 до 20
        minutes = random.randrange(0, 60)
        self.time_string = str(hours) + ":" + str(minutes) #искомое рандомное время


class Items():
    def __init__(self, data, time, **kwargs):  # использовать **kwargs вместо словаря #К:в кваргс идет количество заказанных велосипедов
        self.items = {"bike_1": 3, "bike_2": 4, "bike_3": 5} #К:тут лежат цены
        self.quant = kwargs
        self.total = 0
        self.list_of_items_string = ""
        self.total_bikes_quantity = 0
        self.data = data
        self.time = time

    def total_sum(self):
        for i in self.items:
            self.total += self.items[i] * self.quant[i]
        return self.total

    def total_quantity(self):
        for v in self.quant.values():
            self.total_bikes_quantity += v
        return self.total_bikes_quantity

    def list_of_items(self):
        for k, v in self.quant.items():
            self.list_of_items_string += k
            self.list_of_items_string += " - "
            self.list_of_items_string += str(v)
            self.list_of_items_string += " штук"
            self.list_of_items_string += "\n"
        return self.list_of_items_string

    # скидка от суммы больше 100 = 20%
    # скидка от кол-ва частей от 3 и за каждую следующую +10%, но не больше 40
    # если обе скидки, брать одну, самую большую

    def discount(self):
            self.total_sum = self.total_sum()
            #self.list_of_items_string = self.list_of_items()
            self.total_bikes_quantity_ordered = self.total_quantity()
            if self.total_sum > 100:
                self.discount_amount = self.total_sum * 0.2
            else:
                self.discount_amount = 0
            if self.total_bikes_quantity_ordered > 6:
                self.discount_quantity = self.total_sum * 0.4
            elif self.total_bikes_quantity_ordered >= 3:
                self.discount_quantity = self.total_sum * 0.1 * (self.total_bikes_quantity_ordered - 2)
            else:
                self.discount_quantity = 0
            self.disc_list = [self.discount_amount, self.discount_quantity]
            return self.disc_list

    def __str__(self):
        self.list_of_items_string = self.list_of_items()
        self.total_bikes_quantity_ordered = self.total_quantity()
        self.total = self.total_sum()
        self.disc_list = self.discount()
        return f"{self.list_of_items_string}\n" \
               f"Общая сумма без скидки: {self.total}\n" \
               f"Общее количество: {self.total_bikes_quantity_ordered}\n" \
               f"Скидка: {max(self.disc_list)}\n" \
               f"Общая сумма со скидкой: {self.total_sum - max(self.disc_list)}\n" \
               f"{str(self.data)}, {self.time}"

cal1 = CalendarTimer()
item1 = Items(cal1.random_day, cal1.time_string, bike_1=5, bike_2=7, bike_3=9)
print(item1)