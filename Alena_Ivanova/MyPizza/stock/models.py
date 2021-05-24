from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=20)
    description = models.TextField(max_length=255)
    weight = models.IntegerField()
    price = models.SmallIntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class PizzaDraft(models.Model):
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=20)
    description = models.TextField(max_length=255)
    weight = models.IntegerField()
    price = models.SmallIntegerField()
    active = models.BooleanField(default=True)
    comment = models.CharField(max_length=255)
    author = models.CharField(max_length=20)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kw):
        if self.is_checked:
            Pizza_new = Pizza(
                name=self.name,
                size=self.size,
                description=self.description,
                weight=self.weight,
                price=self.price,
                active=self.active)

            Pizza_new.save()
            PizzaDraft.objects.filter(name=self.name).delete()


# declare a new model with a name "OrdersModel"
class Order(models.Model):
    # fields of the model
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date = models.DateField()
    time_of_delivery = models.TimeField()
    address = models.CharField(max_length=200)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, default=1)
    count = models.IntegerField(default=1)

    # renames the instances of the model
    def __str__(self):
        return f'Order for {self.last_name}, date: {self.date}, time:{self.time_of_delivery}'
