from .models import Order, Choice
from django.shortcuts import render


def index(request):
    orders = Order.objects.all()
    context = {
        'orders': orders,
    }
    return render(request, 'index.html', context)
