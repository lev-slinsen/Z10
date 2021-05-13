from django.shortcuts import render
from django.http import HttpResponse
from django import views
from django.template import loader

from .models import Pizza


def index(request):
    pizzas = Pizza.objects.filter(isActive=True)
    context = {
        'pizzas': pizzas,
    }
    return render(request, 'index.html', context)
