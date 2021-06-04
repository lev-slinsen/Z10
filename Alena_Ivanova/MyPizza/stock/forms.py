from datetime import datetime
from django import forms
from .models import Pizza, Order, PizzaDraft


# creating a form
class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    date = forms.DateField(initial=datetime.today(), widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    time_of_delivery = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}))
    address = forms.CharField(max_length=200)
    pizza_to_choose = forms.ModelChoiceField(queryset=Pizza.objects.all())

class OrderForm(forms.ModelForm):
     # # specify the name of model to use
     class Meta:
         model = Order
         fields = "__all__"


class PizzaDraftForm(forms.ModelForm):
    # # specify the name of model to use
    class Meta:
        model = PizzaDraft
        fields = ('name', 'size', 'description', 'weight',  'price',  'active',  'comment', 'author')



