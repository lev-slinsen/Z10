from django.db import models

# Create your models here
class Pizza(models.Model):
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    weight = models.IntegerField()
    price = models.FloatField()
    active_field = models.BooleanField(default=True)

    def __str__(self):
        return self.name
