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
    price = models.PositiveSmallIntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}:  {self.price}'


class Order(models.Model):
    name = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=False)


    def __str__(self):
        return f'{self.name} '

    @property
    def price(self):
        choices = Choice.objects.filter(order=self.id)
        price_before_discount = 0
        total_count = 0
        for choice in choices:
            total_count = total_count + choice.quantity
            price_before_discount = price_before_discount + choice.product.price * choice.quantity

        return price_before_discount

    @property
    def final_price(self):
        choices = Choice.objects.filter(order=self.id)
        price_before_discount = 0
        total_count = 0
        for choice in choices:
            total_count = total_count + choice.quantity
            price_before_discount = price_before_discount + choice.product.price * choice.quantity

        discount_1 = 0
        discount_2 = 0
        if price_before_discount > 100:
            discount_1 = 20

        if total_count > 3:
            discount_2 = 10

        price_after_discount = (1 - max(discount_1, discount_2)/100) * price_before_discount
        return price_after_discount


class Choice(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)


    def __str__(self):
        return f'{self.order}  {self.product}  {self.quantity}'

    # def quantity1(self):
    #     choices = Choice.objects.all()
    #     for choice in choices:
    #         print(choice.quantity)
    #         return choice.quantity

