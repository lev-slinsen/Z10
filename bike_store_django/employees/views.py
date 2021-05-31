from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Team, Timetable
from datetime import date



def home(request):
    posts = Employee.objects.all()
    tosts = Timetable.objects.all()
    today = date.today()

    return render(request, 'blog/home.html', {'posts': posts, 'tosts': tosts, "today": today})
