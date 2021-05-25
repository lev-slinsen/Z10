from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    active = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    engname = models.CharField(max_length=255)
    size = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    weight = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    comment = models.TextField(default="")
    creator = models.CharField(max_length=255, default="admin")
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name

class Order(models.Model):
    position = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.position}, {self.quantity}"

class ShopingCar(models.Model):
    customer = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    time = models.TimeField()
    date = models.DateField()
    food = models.ManyToManyField(Order)









