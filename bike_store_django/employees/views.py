from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Team, Timetable


def home(request):
    posts = Employee.objects.all()
    tosts = Timetable.objects.all()

    return render(request, 'blog/home.html', {'posts': posts, 'tosts': tosts})
