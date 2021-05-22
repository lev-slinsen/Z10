from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=20)
    description = models.TextField(max_length=255)
    weight = models.IntegerField()
    price = models.FloatField()
    active = models.BooleanField()
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')

    def __str__(self):
        return self.name