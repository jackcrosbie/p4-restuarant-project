from .models import Reservations
from django import forms


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = ('name', 'phone_number', 'email', 'date', 'time', 'number_of_party')
