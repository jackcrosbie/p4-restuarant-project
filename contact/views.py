from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import ContactUs
from .forms import ContactUsForm


class ContactUsFormView(CreateView):
    model = ContactUs()
    template_name = "contact/contact.html"
    form_class = ContactUsForm
    success_url = 'contact_complete/'

    def form_valid(self, form):
        
        return super().form_valid(form)


class ContactUsCompleteView(CreateView):
    template_name = "contact/contact_complete.html"
    success_url = "contact_complete/"
    form_class = ContactUsForm
    model = ContactUs
