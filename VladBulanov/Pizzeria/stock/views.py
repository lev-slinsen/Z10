from django.shortcuts import render
from .models import Pizza


def pizza(request):
    pizzas = Pizza.objects.all()
    return render (request, 'stock/active_p.html', {pizzas})


from .forms import OrderActive
import datetime