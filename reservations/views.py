from django.shortcuts import render
from django.views import generic, View
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from .models import Reservations
from .forms import ReservationForm


# Create your views here.
class ReservationsFormView(FormView):
    template_name = "reservations.html"
    form_class = ReservationForm
    success_url = '/reservations/'

    def form_valid(self, form):
        return super().form_valid(form)
