from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from .models import Choice, Order, Product


class ChoiceForm(ModelForm):
    class Meta:
        model = Choice

        fields = ['order', 'product', 'quantity']


# OrderFormSet = inlineformset_factory(Order, Choice)
# ProductFormSet = inlineformset_factory(Product, Choice)
