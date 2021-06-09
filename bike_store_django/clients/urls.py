from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('<int:order_id>', views.order_information, name='order_information'),
    path('order', views.make_order, name='make_order'),

]
