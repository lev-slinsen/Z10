from django.urls import path
from . import views


urlpatterns = [
    path('', views.pizzas_view, name='home')
    ]