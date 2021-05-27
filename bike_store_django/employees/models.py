from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    salesman = models.BooleanField()
    manager = models.BooleanField()
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')

    def __str__(self):
        return self.name

class Team(models.Model):
    worker = models.ManyToManyField(Employee)

class Timetable(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    day = models.DateField()

