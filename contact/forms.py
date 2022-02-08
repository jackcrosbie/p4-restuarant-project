from .models import ContactUs
from django import forms
from reservations.widgets import DatePickerInput


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'phone_number', 'email', 'date', 'time', 'event', 'message']
        widgets = {
            'date': DatePickerInput(format='%d-%m-%Y'),
        }
