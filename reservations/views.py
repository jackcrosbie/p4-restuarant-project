from django.views.generic.edit import CreateView, UpdateView
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Reservations
from .forms import ReservationForm


# Create your views here.
class ReservationsFormView(CreateView):
    model = Reservations
    template_name = "reservations.html"
    form_class = ReservationForm
    success_url = '/reservations'
    


    def form_valid(self, form):
        
        # this is what the method needs to run as expected when called, otherwise it's missing info it needs
        return super().form_valid(form)


class ReservationUpdateView(UpdateView):
    model = Reservations
    fields = [
        'name', 'phone_number', 'email', 'date', 'time', 'number_of_party'
    ]
    success_url = "reservations/"
    

#class EditReservation():
#     def get(self, request, reservation_id, *args, **kwargs):
#        if request.user.is_authenticated:
#            # Get reservation object based on id
#            reservation = get_object_or_404(
#                Reservation, reservation_id=reservation_id)
