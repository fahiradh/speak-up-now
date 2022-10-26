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
            contactable = 'Y'
        )
        return new_curhat
    
    # Views test
    def test_curhat_view_create(self):
        curhat = self.test_new_curhat()
        self.assertTrue(isinstance(curhat, curhatDong))

    def test_curhat_url_is_exist(self):
        response = Client().get('/curhat/')
        self.assertEqual(response.status_code,200)

    def test_curhat_using_index_func(self):
        found = resolve('/curhat/')
        self.assertEqual(found.func, curhat)

    # # Test curhat page
    # def test_curhat_page_url_is_exist(self):
    #     curhat = self.test_new_curhat()
    #     response = Client().get('/tournament/')
    #     self.assertEqual(response.status_code,200)

    # def test_tournament_page_using_tournament_page_templates(self):
    #     tournament = self.test_model_new_tournament()
    #     response = Client().get('/tournament/')
    #     self.assertTemplateUsed(response, 'championship.html')

    # def test_landing_page_url_is_exist(self):
    #     tournament = self.test_model_new_tournament()
    #     response = Client().get('/tournament/landing/')
    #     self.assertEqual(response.status_code,200)

    # def test_landing_page_using_landing_page_templates(self):
    #     tournament = self.test_model_new_tournament()
    #     response = Client().get('/tournament/landing/')
    #     self.assertTemplateUsed(response, 'champ-landing.html')

    # def test_tournament_page_using_tournament_page_func(self):
    #     tournament = self.test_model_new_tournament()
    #     found = resolve('/tournament/')
    #     self.assertEqual(found.func, champ)
   
    # def test_landing_page_using_landing_page_func(self):
    #     tournament = self.test_model_new_tournament()
    #     found = resolve('/tournament/landing/')
    #     self.assertEqual(found.func, land)




