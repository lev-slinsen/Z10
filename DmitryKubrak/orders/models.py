from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    adress = models.TextField(max_length=255)


    def __str__(self):
        return self.name
