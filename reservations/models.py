""" django Imports """
from django.db import models
from django.core.validators import RegexValidator


time_options = (
    ("12:00", "12pm"),
    ("14:00", "2pm"),
    ("16:00", "4pm"),
    ("18:00", "6pm"),
    ("20:00", "8pm"),
    ("22:00", "10pm"),
    )

party_size = ((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, 5), (6, 6))

""" validates phone numbers """
phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")


class Reservations(models.Model):

    """ reservation form categories and attributes """
    name = models.CharField(max_length=50)
    phone_number = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True)
    email = models.EmailField()
    date = models.DateField()
    time = models.CharField(choices=time_options, default="12pm", max_length=10)
    number_of_party = models.IntegerField(choices=party_size, default=1)
    
    # approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['date']
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        return self.name
