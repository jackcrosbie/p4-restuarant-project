from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Create your models here.
class Reservations(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    number_of_party = models.IntegerField()

    def __str__(self):
        return self.name