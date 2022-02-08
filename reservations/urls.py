from . import views
from django.urls import path
from .views import ReservationsFormView, EditReservationView, ReservationCompleteView, ReservationAccountView, DeleteReservationView


urlpatterns = [
    path('', views.ReservationsFormView.as_view(), name='reservations'),
    path('edit_reservation/', EditReservationView.as_view(), name="edit_reservation"),
    path('reservation_complete/', ReservationCompleteView.as_view(), name="reservation_complete"),
    path('reservations_account/', ReservationAccountView.as_view(), name="reservations_account"),
    path('reservation_delete/', DeleteReservationView.as_view(), name="delete_reservation"),
]
