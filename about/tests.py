from django.test import TestCase
from django.test.client import Client


class PrivacyPolicyView(TestCase):
    urls = 'boomajoom_temp.boomajoom_temp.urls'

    def setUp(self):
        self.client = Client()

    def test_details(self):
        response = self.client.get('/about/privacy-policy/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual((response.context['title']), 'Privacy Policy')


class TermsOfServiceView(TestCase):
    urls = 'boomajoom_temp.boomajoom_temp.urls'

    def setUp(self):
        self.client = Client()

    def test_details(self):
        response = self.client.get('/about/terms-of-service/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual((response.context['title']), 'Terms of Service')