from django.db import models

class Pizza(models.Model):
    active = models.BooleanField()
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    description = models.TextField()
    weight = models.IntegerField()
    price = models.FloatField()