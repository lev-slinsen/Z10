from django.db.backends import sqlite3
from django.shortcuts import render, redirect
from .models import Pizza, Order
from .forms import PizzaForm, OrderForm, ShopingCarForm


def index(request):
    pizzas_list = Pizza.objects.all()
    return render(request, "stock/list.html", {"pizzas_list": pizzas_list})

def select_pizza(request):
    var = str(request)[33:]
    pizza_name = var[:-3]
    pizzas_list = Pizza.objects.all()
    return render(request, "stock/margarita.html", {"pizza_name": pizza_name, "pizzas_list": pizzas_list})

def create_pizza(request):
    error = ""
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "Смотри что пишешь!!!"
    form = PizzaForm()
    return render(request, "stock/create.html", {"form": form, "error": error})

def order_pizza(request):
    error = ""
    if request.method == "POST":
        form_order = OrderForm(request.POST)
        if form_order.is_valid():
            form_order.save()
        else:
            error = "Введите заказ"
    form_order = OrderForm()
    return render(request, "stock/order.html", {"form_order": form_order, "error": error})


def shopingcar(request):
    error = ""
    if request.method == "POST":
        form_shopingcar = ShopingCarForm(request.POST)
        if form_shopingcar.is_valid():
            form_shopingcar.save()
            # connection = sqlite3.connect("db.sqlite3")
            # cursor = connection.cursor()
            # cursor.execute('''DELETE * FROM tab_''',
            # connection.commit()
        else:
            error = "Введите поля"
    form_shopingcar = ShopingCarForm()
    return render(request, "stock/shopingcar.html", {"form_shopingcar": form_shopingcar, "error": error})