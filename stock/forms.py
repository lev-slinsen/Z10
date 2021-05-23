from django import forms
from django.forms import ModelForm

from stock.models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['your_name', 'address', 'pizza']

