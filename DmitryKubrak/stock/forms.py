from django.forms import ModelForm
from .models import CreatePizza


class CreateForm(ModelForm):
    class Meta:
        model = CreatePizza
        fields = ['title', 'description', 'size', 'weight', 'author', 'comment']

