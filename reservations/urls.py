from . import views
from django.urls import path



urlpatterns = [
    path('', views.ReservationsFormView.as_view(), name='reservations'),
     path('<pk>/update', views.ReservationUpdateView.as_view()),
]