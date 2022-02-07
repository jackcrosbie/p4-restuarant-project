from .model import Menu
from django import forms

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu