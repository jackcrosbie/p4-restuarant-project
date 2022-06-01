""" imports from django, models.py and forms.py """
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Reservations
from .forms import ReservationForm


class ReservationsFormView(CreateView):
    """View for creation of reservation form based off reservations model"""
    model = Reservations
    form_class = ReservationForm
    template_name = "reservations/reservations.html"
    success_url = "reservation_complete/"

    def form_valid(self, form):
        """ checking form is valid """
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditReservationView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ edit reservation view allows editing
    of the reservations form for registered users """
    model = Reservations
    form_class = ReservationForm
    template_name = 'reservations/edit_reservation.html'
    success_url = "/reservations/reservations_account/"

    def test_func(self):
        return self.request.user == self.get_object().user        


class ReservationCompleteView(CreateView):
    """ view for when a user finishes the form and successfully submits it """
    model = Reservations
    form_class = ReservationForm
    template_name = "reservations/reservation_complete.html"
    success_url = "/reservation_complete/"


class ReservationAccountView(ListView):
    """ view for users to access their account when logged in """
    template_name = "reservations/reservations_account.html"
    model = Reservations

    def get_context_data(self, **kwargs):
        context = {
            'reservations': self.model.objects.filter(user=self.request.user),
        }
        return context


class DeleteReservationView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ A view to allow a user to delete a reservation """
    model = Reservations
    success_url = "/reservations/"

    def test_func(self):
        return self.request.user == self.get_object().user
