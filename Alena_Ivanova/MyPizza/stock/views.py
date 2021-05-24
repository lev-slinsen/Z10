from django.shortcuts import render
from .models import Pizza
from django.shortcuts import render
from .forms import InputForm, OrderForm, PizzaDraftForm

def index(request):
    pizzas = Pizza.objects.filter(active=True)
    context = {
        'pizzas': pizzas,
    }
    return render(request, 'index.html', context)

# # Create your views here.
# def home_view(request):
#     context = {}
#     context['form'] = InputForm()
#     return render(request, "order.html", context)


def order_view(request):
    context = {}

    # create object of form
    form = OrderForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context['form'] = form
    return render(request, "order.html", context)

def pizza_draft_view(request):
    context = {}

    # create object of form
    form = PizzaDraftForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context['form'] = form
    return render(request, "order.html", context)