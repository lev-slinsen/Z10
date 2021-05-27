from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('order/', views.OrderView.as_view(), name='New_Order'),
    path('custom/', views.CustomPizzaView.as_view(), name='Pizza_from_user')

]