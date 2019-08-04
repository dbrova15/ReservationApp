from django import forms
from django.forms import SelectDateWidget
from django.utils import timezone


class DateForm(forms.Form):
    data_time_req = forms.DateField(widget=SelectDateWidget(), initial=timezone.now())


class BookingForm(forms.Form):
    email_fild = forms.EmailField()
