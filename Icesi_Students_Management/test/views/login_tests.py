from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class LoginTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test', password='test')
        self.user.save()

    def test_login(self):
        response = self.client.post(reverse('signin'), {'username': 'test', 'password': 'test'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('home'))

    def test_login_fail(self):
        response = self.client.post(reverse('signin'), {'username': 'test', 'password': 'test2'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['error'], 'Usuario y/o contrasena incorrecta')

    def test_login_post_empty(self):
        response = self.client.post(reverse('signin'), {'username': '', 'password': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signin.html')
        self.assertEqual(response.context['error'], 'Usuario y/o contrasena incorrecta')

    def test_login_post_empty_username(self):
        response = self.client.post(reverse('signin'), {'username': '', 'password': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signin.html')
        self.assertEqual(response.context['error'], 'Usuario y/o contrasena incorrecta')

    def test_login_post_empty_password(self):
        response = self.client.post(reverse('signin'), {'username': 'test', 'password': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signin.html')
        self.assertEqual(response.context['error'], 'Usuario y/o contrasena incorrecta')


