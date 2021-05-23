from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=20)
    description = models.TextField(max_length=255)
    weight = models.IntegerField()
    price = models.FloatField()
    active = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=False)
    address = models.TextField(max_length=255)
    quantity = models.PositiveSmallIntegerField(default=0)
    choice = models.ManyToManyField(Pizza)
    objects = models.Manager()

    def __str__(self):
        return self.name


class CreatePizza(models.Model):
    title = models.CharField(max_length=30, blank=True)
    description = models.TextField(max_length=255, blank=True)
    checked = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    size = models.CharField(max_length=20)
    weight = models.IntegerField()
    author = models.CharField(max_length=30, blank=True)
    comment = models.TextField(max_length=255, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.title


# class ItemSelection(models.Model):
#     item_type = models.ForeignKey(Pizza, on_delete=models.CASCADE)
#     item_quantity = models.ForeignKey(Quantity, on_delete=models.CASCADE)
#     num = models.SmallIntegerField(default=0)
#     address = models.TextField(max_length=255, default="Pizzeria")
#     objects = models.Manager()
#
#
#     class Meta:
#         unique_together = ('item_quantity', 'item_type')
