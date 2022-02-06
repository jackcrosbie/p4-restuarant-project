from .models import Reservations
from django import forms
from .widgets import DatePickerInput


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = ['name', 'phone_number', 'email', 'date', 'time', 'number_of_party']
        widgets = {
            'date': DatePickerInput(format='%d-%m-%Y'),
        }
