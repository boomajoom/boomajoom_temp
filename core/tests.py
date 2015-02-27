from django.test import TestCase
from django.test.client import Client


class IndexView(TestCase):
    urls = 'boomajoom_temp.boomajoom_temp.urls'

    def setUp(self):
        self.client = Client()

    def test_details(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual((response.context['title']), 'Home')