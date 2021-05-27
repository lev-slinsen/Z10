from django.db import models


class Equipment(models.Model):
    name = models.CharField(max_length=55)
    quantity = models.IntegerField()
    price = models.FloatField()
    discount = models.FloatField()


    def __str__(self):
        return self.name
