import tempfile, unittest
from django.test import TestCase, Client
from django.urls import resolve
from .views import curhat
from .models import curhatDong
from .forms import curhatForm
from django.apps import apps
from curhat.apps import CurhatConfig


# Create your tests here.
class myTest(TestCase):
    # Models test
    def test_new_curhat(self):
        new_curhat = curhatDong.objects.create(
            name = 'Laudya',
            title = 'kejadian tidak etis saat parade',
            description = 'saat parade olim ui kemarin, saya mendapatkan perlakuan kurang etis dari salah satu koor parade fakultas blabla',
            contactable = 'Y',
        )
        return new_curhat
    
    # Views test
    def test_curhat_view_create(self):
        curhat = self.test_new_curhat()
        self.assertTrue(isinstance(curhat, curhatDong))

    def test_curhat_url_is_exist(self):
        response = Client().get('/curhat/')
        self.assertEqual(response.status_code, 200)




