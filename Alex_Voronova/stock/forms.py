
from .models import OrderPizza
from django.forms import ModelForm, TextInput, NumberInput, Select

class OrderForm (ModelForm):

    class Meta:
        model = OrderPizza
        fields = ['first_name', 'last_name', 'address', 'products',  'amount']

        widgets = {
            "first_name": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Введите Ваше имя'

            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Вашу Фамилию'
            }),
            "address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Ваш Адресс'
            }),
            "amount": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите количество пицц'
            }),
            "products": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выбери пиццу'
            })

        }