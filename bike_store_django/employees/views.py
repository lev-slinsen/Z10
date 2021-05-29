from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee


def home(request):
    posts = Employee.name.all()
    return render(request, 'blog/home.html', {'posts':posts})
