from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza


def pizzas_view(request):
    template_name = 'stock/pizzas.html'

    queryset = Pizza.objects.all()
    # print(queryset)

    context = {
        'pizzas': queryset
    }

    return render(request, template_name, context)
