from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormView
from .models import Reservations
from .forms import ReservationForm


# Create your views here.
class ReservationsFormView(FormView):
    template_name = "reservations.html"
    form_class = ReservationForm
    success_url = '/index/'

