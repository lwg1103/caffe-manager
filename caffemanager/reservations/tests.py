from django.test import TestCase
from django.urls import resolve
from reservations.views import home_page
from reservations.models import Reservation


class HomePageTest(TestCase):

    def test_root_url_resolves_homepage(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)

    def test_store_and_retrive_reservation(self):
        first_reservation = Reservation()
        first_reservation.name = "first"
        first_reservation.save()

        second_reservation = Reservation()
        second_reservation.name = "second"
        second_reservation.save()

        saved_reservations = Reservation.objects.all()
        self.assertEqual(2, len(saved_reservations))
        self.assertEqual("first", saved_reservations[0].name)
        self.assertEqual("second", saved_reservations[1].name)

