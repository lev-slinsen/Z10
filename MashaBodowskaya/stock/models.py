from datetime import datetime

from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    weight = models.IntegerField()
    price = models.FloatField()
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    your_name = models.CharField(max_length=100)
    date_time = models.DateTimeField(default=datetime.now)
    address = models.CharField(max_length=255)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)


class CustomPizza(models.Model):
    auth_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    weight = models.IntegerField()
    isConfirmed = models.BooleanField(default=False)