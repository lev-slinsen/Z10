from django.db import models
from django.db.models import Model

class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id}: {self.name}'

class Size(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    weight = models.IntegerField()
    price = models.FloatField()
    active = models.BooleanField(default=False)

    ingredients = models.ManyToManyField(Ingredient)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=200)
    purchase_date = models.DateTimeField(auto_now_add=False)
    address = models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.name


