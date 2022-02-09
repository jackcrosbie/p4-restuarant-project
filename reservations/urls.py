""" imports from danjo and from views.py for template pathing"""
from django.urls import path
from .views import ReservationsFormView, EditReservationView, \
    ReservationCompleteView, ReservationAccountView, DeleteReservationView


urlpatterns = [
    path('', ReservationsFormView.as_view(), name='reservations'),
    path('edit/<slug:pk>/', EditReservationView.as_view(),
         name='edit_reservation'),
    path('reservation_complete/', ReservationCompleteView.as_view(),
         name='reservation_complete'),
    path('reservations_account/', ReservationAccountView.as_view(),
         name='reservations_account'),
    path('delete/<slug:pk>/', DeleteReservationView.as_view(),
         name='delete_reservation'),
]
