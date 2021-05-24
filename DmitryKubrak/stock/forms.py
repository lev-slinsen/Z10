from django.forms import ModelForm
from .models import CreatePizza, Pizza


class CreateForm(ModelForm):
    class Meta:
        model = CreatePizza
        fields = ['title', 'description', 'size', 'weight', 'author', 'comment']

#
class ChoiceForm(ModelForm):
    class Meta:
        model = Pizza
        fields = ['name', 'size', 'description', 'weight']


