from selenium import webdriver
import unittest
import time

class HomepageTest(unittest.TestCase):

    def test_see_title(self):
        self.enter_main_site()
        self.see_application_title()

    # def test_see_no_reservation(self):
    #     self.fail('not implemented yet')
    #
    # def test_add_reservation(self):
    #     self.fail('not implemented yet')
    #
    # def test_delete_reservation(self):
    #     self.fail('not implemented yet')
    #
    # def test_reservation_is_stored(self):
    #     self.fail('not implemented yet')

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def enter_main_site(self):
        self.browser.get("http://localhost:8000")

    def see_application_title(self):
        self.assertIn('Caffe Manager', self.browser.title)

    def wait_n_seconds(self, seconds):
        time.sleep(seconds)

if __name__ == '__main__':
    unittest.main()
