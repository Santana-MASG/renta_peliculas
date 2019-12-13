from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class TestViews(TestCase):
    
    def login(self):
        User.objects.create_user(username='Nena', password='nena123')
        self.client.login(username='Nena', password='nena123')

    def test_validacion_URL_peliculas(self):
        self.login()
        response = self.client.get('/peliculas/')
        self.assertEqual(response.status_code, 200)

    def test_si_se_usa_el_template_renta_peliculas(self):
        self.login()
        response = self.client.get('/peliculas/')
        self.assertTemplateUsed(response,'renta_peliculas.html')   

    def test_nombre_url_peliculas(self):
        self.login()
        response = self.client.get(reverse('peliculas'))
        self.assertEqual(response.status_code, 200)

    def test_boton_rentar_existe_en_peliculas(self):
        self.login()
        response = self.client.get('/peliculas/')
        self.assertInHTML(
            '<button id="rentar" type="submit">Rentar</button>', response.content.decode("utf-8"))
