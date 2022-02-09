from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Reservations
from .forms import ReservationForm


# Create your views here.
class ReservationsFormView(CreateView):
    model = Reservations
    form_class = ReservationForm
    template_name = "reservations/reservations.html"
    success_url = "reservation_complete/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditReservationView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Reservations
    form_class = ReservationForm
    template_name = 'reservations/edit_reservation.html'
    success_url = "/reservations_account/"
    

    def test_func(self):
        return self.request.user == self.get_object().user


class ReservationCompleteView(CreateView):
    model = Reservations
    form_class = ReservationForm
    template_name = "reservations/reservation_complete.html"
    success_url = "/reservation_complete/"
    
    


class ReservationAccountView(ListView):
    template_name = "reservations/reservations_account.html"
    model = Reservations

    def get_context_data(self, **kwargs):
        context = {
            'reservations': self.model.objects.filter(user=self.request.user),
        }
        return context


class DeleteReservationView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ A view to delete an reservation """
    model = Reservations
    success_url = "/reservations_account/"

    def test_func(self):
        return self.request.user == self.get_object().user