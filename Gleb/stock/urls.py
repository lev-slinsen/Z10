from django.urls import path
from . import views

app_name = 'stock'


urlpatterns = [
    path('pizzas/', views.pizzas_view, name='my-pizzas'),
]
