from django.db import models
class Pizza(models.Model):
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    weight = models.IntegerField()
    price = models.FloatField()
    active = models.BooleanField()
# Create your models here.
    def __str__ (self):
        return  self.name