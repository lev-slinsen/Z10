from .models import Pizza, Order, ShopingCar
from django.forms import ModelForm

class PizzaForm(ModelForm):
    class Meta:
        model = Pizza
        fields = ["name", "engname", "description", "ingredients", "comment", "creator"]

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["position", "quantity"]

class ShopingCarForm(ModelForm):
    class Meta:
        model = ShopingCar
        fields = ["customer", "adress", "time", "date", "food"]


