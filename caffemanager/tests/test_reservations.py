from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time
from datetime import date
from django.test import tag
from phonenumber_field.phonenumber import PhoneNumber

from reservations.models import Reservation


@tag('fnc')
class ReservationsTest(StaticLiveServerTestCase):

    def test_see_no_reservations_at_start(self):
        self.__enter_reservations_page()
        self.__see_reservations_list_header()
        self.__see_x_reservations_on_list(0)

    def test_add_reservation(self):
        self.__enter_reservations_page()
        self.__see_x_reservations_on_list(0)
        self.__add_reservation_to_the_list("new")
        self.__see_x_reservations_on_list(1)
        self.__see_reservation_with_name("new")

    def test_add_two_reservations(self):
        self.__enter_reservations_page()
        self.__see_x_reservations_on_list(0)
        self.__add_reservation_to_the_list("first", "2020-01-01")
        self.__add_reservation_to_the_list("second", "2020-01-02", phone="+48223456789")
        self.__see_x_reservations_on_list(2)
        self.__see_reservation_with_name("first")
        self.__see_reservation_with_name("second")

    def test_delete_reservation(self):
        self.__there_is_a_reservation("first")
        self.__there_is_a_reservation("second")
        self.__enter_reservations_page()
        self.__delete_reservation("first")
        self.__see_x_reservations_on_list(1)
        self.__see_reservation_with_name("second")

    def test_see_reservation_details(self):
        self.__there_is_a_reservation("first", date(2020, 1, 1), 13, PhoneNumber.from_string("+48123456789"))
        self.__enter_reservations_page()
        self.__enter_reservation_details_page("first")
        self.__see_reservation_details("first", "2020-01-01", "13", "+48123456789")

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def __enter_reservations_page(self):
        self.browser.get(self.live_server_url + "/reservations")

    def __see_reservations_list_header(self):
        self.assertEqual('Reservations', self.browser.find_element_by_id('reservations-header').text)

    def __add_reservation_to_the_list(self, name, date="2020-01-01", table="1", phone="+48123456789"):
        self.browser.find_element_by_id('id_name').send_keys(name)
        self.browser.find_element_by_id('id_date').send_keys(date)
        self.browser.find_element_by_id('id_table').send_keys(table)
        self.browser.find_element_by_id('id_telephone').send_keys(phone)
        self.browser.find_element_by_id('submit-button').click()
        time.sleep(1)

    def __see_reservation_with_name(self, name):
        reservations = self.browser.find_elements_by_class_name('reservation-item')
        self.assertTrue(any(name in reservation.text for reservation in reservations))

    def __see_x_reservations_on_list(self, x):
        self.assertEqual(x, len(self.browser.find_elements_by_class_name('reservation-item')))

    def __delete_reservation(self, name):
        reservations = self.browser.find_elements_by_class_name('reservation-item')
        for reservation in reservations:
            if name in reservation.text:
                reservation.find_element_by_class_name("delete-link").click()
                break

    def __enter_reservation_details_page(self, name):
        reservations = self.browser.find_elements_by_class_name('reservation-item')
        for reservation in reservations:
            if name in reservation.text:
                reservation.find_element_by_class_name("details-link").click()
                break

    def __see_reservation_details(self, name, date, table, phone):
        self.assertTrue(name in self.browser.find_element_by_id('reservation-name').text)
        self.assertTrue(date in self.browser.find_element_by_id('reservation-date').text)
        self.assertTrue(table in self.browser.find_element_by_id('reservation-table').text)
        self.assertTrue(phone in self.browser.find_element_by_id('reservation-phone').text)

    def __there_is_a_reservation(self, name, date=None, table=None, phone=None):
        reservation = Reservation()
        reservation.name = name
        reservation.date = date
        reservation.table = table
        reservation.telephone = phone
        reservation.save()

