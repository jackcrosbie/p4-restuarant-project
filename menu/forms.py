""" django and model imports """
from django import forms
from .models import Menu


class MenuForm(forms.ModelForm):
    """ menu form class """
    class Meta:
        """ meta data for menu form """
        model = Menu
        fields = ['img_one', 'img_two', 'img_three', 'img_four']
