from . import views
from django.urls import path

urlpatterns = [
    path('', views.MenuFormView.as_view(), name='menu')
]