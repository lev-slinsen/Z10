from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=20)
    description = models.TextField(max_length=255)
    weight = models.IntegerField()
    price = models.FloatField(default=15.0)
    active = models.BooleanField(default=False)
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


class Order(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField('order date', auto_now_add=False)
    address = models.TextField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Choice(models.Model):
    question = models.ForeignKey(Order, on_delete=models.CASCADE)
    choice_text = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    CHOICES = (
        ('s', 'small'),
        ('m', 'medium'),
        ('l', 'large'),
        ('xl', 'x-large')
    )
    size = models.CharField(max_length=300, choices=CHOICES)
