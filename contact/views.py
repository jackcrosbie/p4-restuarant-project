from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import ContactUs
from .forms import ContactUsForm


class ContactUsFormView(CreateView):
    model = ContactUs()
    template_name = "contact.html"
    form_class = ContactUsForm
    succes_url = '/contact.html/'

    def form_valid(self, form):
        
        return super().form_valid(form)
