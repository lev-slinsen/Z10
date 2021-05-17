from django.shortcuts import render

def view_p(request):
    context = {
        "cheese pizza": 1,
    }

    return render(request, "pizza.html", context)
