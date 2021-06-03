from django.shortcuts import render
from django.http import HttpResponse
from django import views
from django.template import loader

from .models import Stock


def stock(request):
    used_parts = Stock.objects.all()
    context = {
        'used_parts': used_parts,
    }
    return render(request, 'stock.html', context)


from django.views.generic import CreateView
from .forms import OrderForm


class OrderView(CreateView):
    form_class = OrderForm
    success_url = "/order"  # куда переадресовать пользователя после успешной отправки формы
    template_name = 'order.html'