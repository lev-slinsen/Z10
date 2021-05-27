from django.db import models


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
    confirmed = models.BooleanField(default=False)

    ingredients = models.ManyToManyField(Ingredient)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
