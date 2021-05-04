# --- клиенты, чеки, покупки
# время покупки
# список товаров
# скидка от суммы больше 100 = 20%
# скидка от кол-ва частей от 3 и за каждую следующую +10%, но не больше 40
# если обе скидки, брать одну, самую большую
'''
дата: 01.30.2022
время покупки: 12.30
список товаров: объекты
сумма: 420
сумма со скидкой: 69
'''


class Items():
    def __init__(self, quant={"bike_1": 6, "bike_2": 2, "bike_3": 5}):  # использовать **kwargs вместо словаря
        self.items = {"bike_1": 3, "bike_2": 4, "bike_3": 5}
        self.quant = quant
        self.total = 0
        self.string=""

    def total_sum(self):
        for i in self.items:
            self.total += self.items[i] * self.quant[i]
        return self.total

    def list_of_items(self):
        for k, v in self.quant.items():
            self.string += k
            self.string += " - "
            self.string += str(v)
            self.string += "\n"
        return self.string

    def discount(self):
            self.total_sum = self.total_sum()

            if self.total_sum > 100:
                self.discount_amount = self.total_sum * 0.2
            else:
                self.discount_amount = self.total_sum
            self.quantity_of_purshace = len(self.quant)
            if self.quantity_of_purshace >= 3:
                self.discount_quantity = self.total_sum * 0.1 * len(self.quant)
            elif len(self.quant) > 4:
                self.discount_quantity = self.total_sum * 0.4
            print(self.discount_amount)
            print(self.discount_quantity)


class Receipt(Items):
    def __init__(self, date, time):
        self.date = date
        self.time = time

    def __str__(self):
        return f'Date: {self.date}, Time: {self.time}'


item1 = Items()
date_of_purshace = Receipt("10-10-2020", "10:01:59")
print(date_of_purshace)
print(item1.list_of_items())
print(item1.total_sum())
print(item1.discount())
