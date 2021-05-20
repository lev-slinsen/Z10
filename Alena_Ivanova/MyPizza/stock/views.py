from django.shortcuts import render
from .models import Pizza


def index(request):
    pizzas = Pizza.objects.filter(active=True)
    context = {
        'pizzas': pizzas,
    }
    return render(request, 'index.html', context)
