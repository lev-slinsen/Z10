from django.urls import path
from .views import index, order_view, pizza_draft_view

urlpatterns = [
    path('', index),
    path('order/', order_view),
    path('pizzadraft/', pizza_draft_view),
]
