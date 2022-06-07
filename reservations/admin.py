""" django and model imports """
from django.contrib import admin
from .models import Reservations

# Register your models here.


@admin.register(Reservations)
class ReservationAdmin(admin.ModelAdmin):
    """ display and search fields for admin page """
    list_display = ('name', 'date', 'time', 'number_of_party')
    list_filter = ('name', 'date')
    search_fields = ['name', 'date', 'time', 'email']

    def approve_reservations(self, request, queryset):
        """ update reservations on admin panel """
        queryset.update(approve=True)
