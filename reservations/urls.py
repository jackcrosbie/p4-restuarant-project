from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReservationsFormView.as_view(), name='reservations')
]
