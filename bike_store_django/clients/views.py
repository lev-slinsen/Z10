from .models import Order, Choice
from django.shortcuts import render


def index(request):
    orders = Order.objects.all()
    # for order in orders:
    #     print(order.id)
    #     choices = Choice.objects.filter(order=order.id)
    #     price_before_discount = 0
    #     products = []
    #     total_count = 0
    #     for choice in choices:
    #         products.append(choice.product)
    #         total_count = total_count + choice.quantity
    #         price_before_discount = price_before_discount + choice.product.price * choice.quantity
    #
    #     discount_1 = 0
    #     discount_2 = 0
    #     if price_before_discount > 100:
    #         discount_1 = 20
    #
    #     if total_count > 3:
    #         discount_2 = 10
    #
    #     price_after_discount = (1 - max(discount_1, discount_2)/100) * price_before_discount
    #     order.price = price_before_discount
    #     order.price_after_discount = price_after_discount
    #     order.save()
    context = {
        'orders': orders,
    }
    return render(request, 'index.html', context)
