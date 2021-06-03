from django import forms
from django.forms import ModelForm

from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['part', 'qty']

    s = forms.model_to_dict()

