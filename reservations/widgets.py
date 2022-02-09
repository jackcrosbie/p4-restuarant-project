""" django imports """
from django import forms


class DatePickerInput(forms.DateInput):
    """ Datepicker for reservation and contact form """
    input_type = 'date'
