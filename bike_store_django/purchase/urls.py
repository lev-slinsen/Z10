from django.urls import path

from . import views

urlpatterns = [
    path('', views.stock, name='stock'),
    path('order/', views.OrderView.as_view(), name='New_Order'),

]