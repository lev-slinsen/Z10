from django.shortcuts import render
from django.views import View
from .models import Pizza
# Create your views here.


class PizzaView(View):
    pass

def index(request):

    pizzas_list = Pizza.objects.order_by("active")
    return render(request,"list.html",{"pizzas_list":pizzas_list})