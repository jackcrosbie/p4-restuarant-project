""" django Imports """
from django.db import models
from django.contrib.auth.models import User


class Reservations(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    number_of_party = models.IntegerField()
    # approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['date']
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        return self.name
