from django.db import models
from datetime import datetime


class Stock(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Order(models.Model):
    part = models.ForeignKey(Stock, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()
    date = models.DateField(default=datetime.now)

    @property
    def price(self):
        total_price = self.part.price * self.qty
        return total_price





        """# --- закупки, оборудование
# заявки на оборудование принимаются когда накапливается 20 или больше частей всего
# или 10 одинаковых частей

# на 7 или больше одинаковых частей идёт скидка 15%
# нужно высчитать сумму деталей и выписать документ с полным перечнем и общей стоимостью на дату

'''
дата: 01.30.2022
части: объекты
сумма: 100500
сумма со скидкой: 9000"""


