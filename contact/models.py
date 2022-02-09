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


event_type = (
    ("private_function", "Private Function"),
    ("large_group_booking", "Large Group Booking"),
    ("feedback_comment", "Feedback or Comment"),
    ("other", "Other"),
)

""" validates phone numbers """
phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")


class ContactUs(models.Model):

    """ reservation form categories and attributes """
    name = models.CharField(max_length=50)
    phone_number = models.CharField(
        validators=[phoneNumberRegex], max_length=16, unique=True
        )
    email = models.EmailField()
    date = models.DateField()
    time = models.CharField(
        choices=time_options, default="12pm", max_length=10
        )
    event = models.CharField(choices=event_type, max_length=50)
    message = models.TextField()
