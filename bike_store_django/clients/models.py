from django.db import models


class Clients(models.Model):
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

    # @property
    # def final_price(self):
    #     if self.price > 100:


class Order(models.Model):
    name = models.ForeignKey(Clients, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=False)
    price = models.PositiveSmallIntegerField(default=0)


class Choice(models.Model):
    question = models.ForeignKey(Order, on_delete=models.CASCADE)
    choice_text = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    # price = Product.price * quantity



