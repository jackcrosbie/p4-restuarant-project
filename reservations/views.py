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
    """ pass """
    model = Reservations
    template_name = "reservations/reservations.html"
    form_class = ReservationForm
    success_url = "reservation_complete/"

    # def get(self, request):
    #     r = Reservations.objects.all()
    #     print(r)
    #     return render(request, self.template_name, { 'object_list': r})
    


    def form_valid(self, form):
        form.instance.user = self.request.user
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
    model = Reservations
    template_name = "reservations/reservations_account"

    

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
    success_url = "/reservations/"

    def test_func(self):
        return self.request.user == self.get_object().user