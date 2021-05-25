from django.conf.urls import url

from . import views

app_name = 'stock'

urlpatterns = [
    url(r'^pizzas/\D+/', views.select_pizza),
    url(r'^create$', views.create_pizza),
    url(r'^order/shopingcar$', views.shopingcar),
    url(r'^order$', views.order_pizza),
    url(r'^$', views.index, name='index'),
]
