from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pizza, Order
from .forms import CreateForm
from .models import CreatePizza


def pizzas_view(request):
    template_name = 'stock/pizzas.html'
    queryset = Pizza.objects.all()
    context = {
        'pizzas': queryset
    }

    return render(request, template_name, context)


def order(request):
    orders = Order.objects.all()
    return render(request, 'stock/orders.html', {'orders': orders})


def create_pizza(request):
    if request.method == 'GET':
        return render(request, 'stock/create.html', {'form': CreateForm()})
    else:
        form = CreateForm(request.POST)
        new_pizza = form.save(commit=False)
        new_pizza.save()
        return redirect('current')


def current_pizza(request):
    pizzas = CreatePizza.objects.all()
    return render(request, 'stock/current.html', {'pizzas': pizzas})
