from django.urls import path
from . import views
from .views import ContactUsFormView, ContactUsCompleteView


urlpatterns = [
    path('', ContactUsFormView.as_view(), name='contact'),
    path('contact_complete/', ContactUsCompleteView.as_view(), name='contact_complete')
]