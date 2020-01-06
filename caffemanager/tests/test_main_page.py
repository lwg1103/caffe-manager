from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import tag


@tag('fnc')
class HomepageTest(StaticLiveServerTestCase):

    def test_see_title(self):
        self.__enter_main_site()
        self.__see_application_title()

    def test_reservations_link(self):
        self.__enter_main_site()
        self.__i_click_reservations_link()
        self.__im_on_reservations_page()

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(1)

    def tearDown(self):
        self.browser.quit()

    def __enter_main_site(self):
        self.browser.get(self.live_server_url)

    def __i_click_reservations_link(self):
        self.browser.find_element_by_id("reservations_link").click()

    def __im_on_reservations_page(self):
        self.assertEqual(self.browser.current_url, self.live_server_url + "/reservations")

    def __see_application_title(self):
        self.assertIn('Caffe Manager', self.browser.title)

