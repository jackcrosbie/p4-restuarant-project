from .models import Menu
from django import forms

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['img_one', 'img_two', 'img_three', 'img_four']