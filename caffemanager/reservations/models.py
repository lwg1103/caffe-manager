from django.db import models


class Reservation(models.Model):
    name = models.CharField(max_length=30)
