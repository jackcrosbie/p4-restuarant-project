from django.shortcuts import render
from django import forms
from .models import Reservations
from .forms import ReservationForm


# Create your views here.
class ReservationsPage(forms.Form):
    name = forms.CharField(max_length=50)
    phone_number = forms.IntegerField()
    email = forms.EmailField()
    date = forms.DateField()
    time = forms.TimeField()
    number_of_party = forms.IntegerField()