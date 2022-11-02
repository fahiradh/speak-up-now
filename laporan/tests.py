from django.test import TestCase
from django.test import Client
from django.urls import reverse


# Create your tests here.
class laporanTest(TestCase):
    def test_show_json(self):
        client = Client()
        response = client.get(reverse('laporan:show_json'))
        self.assertEqual(response.status_code, 302)

    def test_show_laporan(self):
        client = Client()
        response = client.get(reverse('laporan:show_laporan'))
        self.assertEqual(response.status_code, 302)

    def test_detail_laporan(self):
        client = Client()
        response = client.get(reverse('laporan:detail_laporan', kwargs={'id':1}))
        self.assertEqual(response.status_code, 302)
