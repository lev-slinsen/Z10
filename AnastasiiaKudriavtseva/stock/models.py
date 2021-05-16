from django.db import models
from django.db.models import Model

class Pizza(models.Model):
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=20)
    description = models.TextField(max_length=255)
    weight = models.IntegerField()
    price = models.FloatField()
    active = models.BooleanField()

    def __str__(self):
        return self.name
