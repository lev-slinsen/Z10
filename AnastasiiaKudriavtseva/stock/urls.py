from django.contrib import admin
from django.urls import path
from .views import Pizza
from . import views


app_name = 'stock'

urlpatterns = [
    path('pizzas/', Pizza),
    path('pizzas/', views.pizzas_view, name='my-pizzas'),
    path('place_order/', views.place_order.html, name='place-order'),

]
