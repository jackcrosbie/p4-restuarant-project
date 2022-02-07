from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Menu
from .forms import MenuForm

# Create your views here.
class MenuFormView(CreateView):
    model = Menu()
    template_name = 'menu.html'
    form_class = MenuForm
    
    def form_valid(self, form):
        
        # this is what the method needs to run as expected when called, otherwise it's missing info it needs
        return super().form_valid(form)