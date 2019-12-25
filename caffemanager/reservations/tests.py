from django.test import TestCase
from django.urls import resolve
from reservations.views import home_page
from django.http import HttpRequest

class HomePageTest(TestCase):

    def test_root_url_resolves_homepage(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)

    def test_home_page_contains_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertTrue(response.content.endswith(b'</html>'))