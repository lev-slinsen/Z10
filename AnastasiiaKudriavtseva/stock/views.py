from .models import Pizza
from django.shortcuts import render
from .forms import PurchaseForm
from django.http import HttpResponseRedirect


def pizzas_view(request):
    template_name = 'stock/pizzas.html'

    queryset = Pizza.objects.filter(active=True)

    context = {
        'pizzas': queryset,
    }

    return render(request, template_name, context)

def place_order(request):
    submitted = False
    if request.method == "POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/place_order?submitted=True')
    else:
        form = PurchaseForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'view.place_order.html', {'form': form, 'submitted': submitted})
