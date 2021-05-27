from django.forms import ModelForm
from .models import CreatePizza, Choice, Pizza


class CreateForm(ModelForm):
    class Meta:
        model = CreatePizza
        fields = ['title', 'description', 'size', 'weight', 'author', 'comment']


class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text', 'quantity', 'size']

