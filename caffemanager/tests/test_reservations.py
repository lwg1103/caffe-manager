from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time
from django.test import tag


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
        self.__add_reservation_to_the_list("first")
        self.__add_reservation_to_the_list("second")
        self.__see_x_reservations_on_list(2)
        self.__see_reservation_with_name("first")
        self.__see_reservation_with_name("second")

    def test_delete_reservation(self):
        self.__enter_reservations_page()
        self.__see_x_reservations_on_list(0)
        self.__add_reservation_to_the_list("first")
        self.__add_reservation_to_the_list("second")
        self.__delete_reservation("first")
        self.__see_x_reservations_on_list(1)
        self.__see_reservation_with_name("second")

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(1)

    def tearDown(self):
        self.browser.quit()

    def __enter_reservations_page(self):
        self.browser.get(self.live_server_url + "/reservations")

    def __see_reservations_list_header(self):
        self.assertEqual('Reservations', self.browser.find_element_by_id('reservations-header').text)

    def __add_reservation_to_the_list(self, name):
        input_field = self.browser.find_element_by_id('new_reservation_name_input')
        input_field.send_keys(name + Keys.ENTER)
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
                reservation.find_element_by_tag_name("a").click()
                break
