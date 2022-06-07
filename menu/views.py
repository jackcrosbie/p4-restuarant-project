""" imports for django, models and forms """
from django.views.generic.edit import CreateView
from .models import Menu
from .forms import MenuForm


class MenuFormView(CreateView):
    """ view for menu form"""
    model = Menu()
    template_name = 'menu/menu.html'
    form_class = MenuForm

    def form_valid(self, form):
        """ form validation """
        return super().form_valid(form)
