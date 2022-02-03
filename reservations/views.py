from django.shortcuts import render
from django.views import generic, View
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from .models import Reservations
from .forms import ReservationForm


# Create your views here.
class ReservationsFormView(CreateView):
    model = Reservations
    template_name = "reservations.html"
    form_class = ReservationForm
    success_url = '/reservations/'

    
    def form_valid(self, form):
        
        print("Form Submitted Successfully")
        # this is what the method needs to run as expected when called, otherwise it's missing info it needs
        return super().form_valid(form)
