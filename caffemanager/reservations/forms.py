from django import forms
from django.forms import ModelForm
from reservations.models import Reservation


class ReservationForm(ModelForm):

    class Meta:
        model = Reservation
        fields = ["name", "table", "date", "telephone"]

