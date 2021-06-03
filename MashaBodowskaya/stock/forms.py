from django import forms
from django.forms import ModelForm

from stock.models import Order, CustomPizza


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['your_name', 'address', 'pizza']


class CustomObject(ModelForm):
    class Meta:
        model = CustomPizza
        fields = ['auth_name', 'name', 'description', 'weight']