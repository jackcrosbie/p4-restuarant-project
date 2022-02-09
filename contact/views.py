""" imports from django, models.py and forms.py """
from django.views.generic.edit import CreateView
from .models import ContactUs
from .forms import ContactUsForm


class ContactUsFormView(CreateView):
    """ view for generating the contact form """
    model = ContactUs()
    template_name = "contact/contact.html"
    form_class = ContactUsForm
    success_url = 'contact_complete/'


class ContactUsCompleteView(CreateView):
    """ view for once the contact form has been completed """
    template_name = "contact/contact_complete.html"
    success_url = "contact_complete/"
    form_class = ContactUsForm
    model = ContactUs
