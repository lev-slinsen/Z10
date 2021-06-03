from django import forms
from .models import Order

class PurchaseForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('name', 'purchase_date', 'address')
