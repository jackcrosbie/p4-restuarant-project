""" imports from Django, models.py and widgets """
from django import forms
from .models import Reservations
from .widgets import DatePickerInput


class ReservationForm(forms.ModelForm):
    """ implementing the from the model in models.py """
    class Meta:
        """ setting form fields and telling form where to get model """
        model = Reservations
        fields = [
            'name', 'phone_number', 'email', 'date', 'time', 'number_of_party'
            ]
        widgets = {
            'date': DatePickerInput(format='%d-%m-%Y'),
        }
