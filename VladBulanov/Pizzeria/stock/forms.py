from django import forms
from .models import Pizza


class OrderActive(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['first_name', 'last_name', 'date', 'time', 'address']