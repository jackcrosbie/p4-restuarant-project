from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView
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
    def get(self, request, *args, **kwargs):
        reservation = Reservations.objects.get(uuid=kwargs['uuid'])
        form = EditReservationForm(initial={"name": reservation.name, "email": reservation.email, })
        return render(request, "reservation/edit-reservation.html", {"form": form})
    

class ReservationCompleteView(CreateView):
    template_name = "reservations/reservation_complete.html"
    success_url = "/reservation_complete/"
    form_class = ReservationForm
    model = Reservations


class RetrieveReservationView(ListView):
    model = ReservationForm
    template_name = "reservations/reservations_account"

class ReservationAccountView(TemplateView):
    template_name = "reservations/reservations_account.html"

class DeleteReservationView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ A view to delete an reservation """
    model = Reservations
    success_url = "/reservations/"

    def test_func(self):
        return self.request.user == self.get_object().user