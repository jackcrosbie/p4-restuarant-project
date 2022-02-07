from . import views
from django.urls import path
from .views import ReservationsFormView, EditReservationView, ReservationCompleteView, ReservationAccountView



urlpatterns = [
    path('', views.ReservationsFormView.as_view(), name='reservations'),
    path('edit/<slug:pk>/', EditReservationView.as_view(), name="edit_reservation"),
    path('complete/<slug:pk>/', ReservationCompleteView.as_view(), name="reservation_complete"),
    path('reservations_account/', ReservationAccountView.as_view(), name="reservations_account"),
]