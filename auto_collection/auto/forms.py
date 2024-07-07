from django import forms
from .models import Car
from django.core.exceptions import ValidationError

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'year', 'price']


