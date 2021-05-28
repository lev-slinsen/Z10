from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    salesman = models.BooleanField()
    manager = models.BooleanField()
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')

    def __str__(self):
        return self.name

class Team(models.Model):
    team_name = models.CharField(max_length=255)
    worker = models.ForeignKey(Employee, related_name = 'cashier', on_delete=models.CASCADE)
    worker2 = models.ForeignKey(Employee, related_name = 'boulangerie', on_delete=models.CASCADE)
    worker3 = models.ForeignKey(Employee, related_name = 'mainsalesman', on_delete=models.CASCADE)

    def __str__(self):
        return self.team_name

class Timetable(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    day = models.DateField()
    is_working_day = models.BooleanField()
