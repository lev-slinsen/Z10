from django.shortcuts import render
from .models import Pizza

def index(request):
    pizzas_list = Pizza.objects.order_by("active")
    return render(request, "list.html", {"pizzas_list": pizzas_list})
