from datetime import datetime

from django.core.validators import MinValueValidator
from django.db import models


class Stock(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Order(models.Model):
    parts = models.ManyToManyField(Stock)
    qty = models.PositiveIntegerField(validators=[MinValueValidator(20)])
    date = models.DateField(default=datetime.now)

    @property
    def price(self):
        # total_price = self.parts.price * self.qty
        return 1
