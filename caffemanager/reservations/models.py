from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Reservation(models.Model):
    TABLE_NUMBERS = [(1, 1), (2, 2), (3, 3)] #to be extended
    name = models.CharField(max_length=30)
    table = models.SmallIntegerField(null=True, blank=False, choices=TABLE_NUMBERS)
    date = models.DateTimeField(null=True, blank=False)
    telephone = PhoneNumberField(null=True, blank=False, unique=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['table', 'date'], name='unique_booking')
        ]

