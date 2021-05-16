from django.shortcuts import render
from .models import Pizza

def pizza(request):
    pizzas = Pizza.objects.all()
    return render (request, 'stock/pizza.html', {'пиццы':pizzas})

