from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pizza, Order, Choice
from .forms import CreateForm
from .models import CreatePizza


""" Пиццы в наличии (активные) """
def pizzas_view(request):
    template_name = 'stock/pizzas.html'
    queryset = Pizza.objects.all()
    context = {
        'pizzas': queryset
    }

    return render(request, template_name, context)


""" Заказ """
def order(request):
    orders = Choice.objects.all()
    orders2 = Order.objects.all()
    context = {
        'orders': orders,
        'orders2': orders2
    }
    return render(request, 'stock/orders.html', context)


""" Создаем новую пиццу """
def create_pizza(request):
    if request.method == 'GET':
        return render(request, 'stock/create.html', {'form': CreateForm()})
    else:
        form = CreateForm(request.POST)
        new_pizza = form.save(commit=False)
        new_pizza.save()
        return redirect('current')


""" Текущие заявки на изготовление пиццы """
def current_pizza(request):
    pizzas = CreatePizza.objects.all()
    return render(request, 'stock/current.html', {'pizzas': pizzas})
