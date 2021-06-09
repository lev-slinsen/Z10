from .models import Order, Choice, Product
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ChoiceForm
from django.forms import inlineformset_factory


def index(request):
    orders = Order.objects.all()
    context = {
        'orders': orders,
    }
    return render(request, 'index.html', context)


def order_information(request, order_id):
    x = Choice.objects.filter(order_id=order_id)
    """ чтобы добыть цену и цену после скидки берем из первого элемента """
    item1 = x[0]
    context = {
         'x': x,
         'item1': item1,
    }
    return render(request, 'order_information.html', context)


def make_order(request):
    product = Product.objects.all()
    ChioceFormSet = inlineformset_factory(Order, Choice, fields=('order', 'product', 'quantity'))
    formset = ChioceFormSet()

    form = ChoiceForm(initial={'product': product})
    if request.method == 'GET':
        return render(request, 'make_order.html', {'form': formset})
    else:
        form = ChoiceForm(request.POST)
        new_order = form.save(commit=False)
        new_order.save()
        return redirect('home')
