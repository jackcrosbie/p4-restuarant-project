from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Reservations
from .forms import ReservationForm


# Create your views here.
class ReservationsFormView(CreateView):
    model = Reservations
    template_name = "reservations/reservations.html"
    form_class = ReservationForm
    success_url = "reservation_complete/"
    


    def form_valid(self, form):
        return super().form_valid(form)


class EditReservationView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Reservations
    template_name = "reservations/edit_reservations.html"
    form_class = ReservationForm
    success_url = "/reservation_complete/"

    def test_func(self):
        return self.request.user == self.get_object().user
    

class ReservationCompleteView(CreateView):
    template_name = "reservations/reservation_complete.html"
    success_url = "/reservation_complete/"
    form_class = ReservationForm
    model = Reservations


class ReservationAccountView(TemplateView):
    template_name = "reservations/reservations_account.html"
