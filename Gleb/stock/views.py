from django.shortcuts import render
from .models import Pizza


def pizzas_view(request):
    template_name = 'stock/pizzas.html'

    queryset = Pizza.objects.filter(confirmed=True)

    context = {
        'pizzas': queryset,
    }

    return render(request, template_name, context)
