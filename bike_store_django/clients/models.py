from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=20)
    description = models.TextField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.SmallIntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}:  {self.price}'


class Order(models.Model):
    name = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=False)
    price = models.PositiveSmallIntegerField(default=0)
    price_after_discount = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.name}  {self.price}  {self.date}'

class Choice(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.order}  {self.product}  {self.quantity}'


