from django.contrib import admin
from .models import Reservations

# Register your models here.

@admin.register(Reservations)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'number_of_party')
    list_filter = ('name', 'date')
    search_fields = ['name', 'date', 'time', 'email']