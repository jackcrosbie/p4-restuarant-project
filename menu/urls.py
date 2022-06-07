""" imports from views and django """
from django.urls import path
from . import views


urlpatterns = [
    path('', views.MenuFormView.as_view(), name='menu')
]
