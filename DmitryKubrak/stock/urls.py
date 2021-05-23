from django.urls import path
from . import views


urlpatterns = [
    path('', views.pizzas_view, name='home'),
    path('orders/', views.order, name='orders'),
    path('create/', views.create_pizza, name='create'),
    path('current/', views.current_pizza, name='current'),
    ]