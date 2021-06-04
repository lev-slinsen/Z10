from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255)
    # startdate = models.DateField()
    salesman = models.BooleanField()
    manager = models.BooleanField()
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        if self.manager:
            self.position = "менеджер"
        else:
            self.position = "продавец"
        return f"{self.name}, {self.position}"


class Team(models.Model):
    worker = models.ForeignKey(Employee, related_name='cashier', on_delete=models.CASCADE)
    worker2 = models.ForeignKey(Employee, related_name='boulangerie', on_delete=models.CASCADE)
    worker3 = models.ForeignKey(Employee, related_name='mainsalesman', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.worker} / {self.worker2} / {self.worker3}"


class Timetable(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    day = models.DateField()
    is_working_day = models.BooleanField()
    manager = models.ForeignKey(Employee, related_name='incharge', on_delete=models.CASCADE, null=True)

    def __str__(self):
        if self.is_working_day:
            self.response = f"{self.team} / {self.manager} - {self.day} - c 12 до 8"
        else:
            self.response = f"{self.team} / {self.manager} - {self.day} - выходной"
        return self.response
