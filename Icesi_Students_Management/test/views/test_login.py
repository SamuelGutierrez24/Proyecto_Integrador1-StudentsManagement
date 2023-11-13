from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class SigninTestCase(TestCase):
    def setUp(self):
        # Create a test user with different roles for testing
        User = get_user_model()
        self.user1 = User.objects.create_user(username='user1', password='password1', rol=0)
        self.user2 = User.objects.create_user(username='user2', password='password2', rol=2)
        self.user3 = User.objects.create_user(username='user3', password='password3', rol=3)
        self.user4 = User.objects.create_user(username='user4', password='password4', rol=4)
        self.user5 = User.objects.create_user(username='user5', password='password5', rol=5)
        self.user6 = User.objects.create_user(username='user6', password='password6', rol=6)
        self.user7 = User.objects.create_user(username='user7', password='password7', rol=7)

    def test_get_request(self):
        response = self.client.get(reverse('signin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signin.html')

    def test_valid_post_request(self):
        data = {
            'username': 'user1',
            'password': 'password1'
        }
        response = self.client.post(reverse('signin'), data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertRedirects(response, reverse('home'))

    def test_invalid_post_request(self):
        data = {
            'username': 'user1',
            'password': 'incorrect'
        }
        response = self.client.post(reverse('signin'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signin.html')
        self.assertContains(response, 'Usuario y/o contrasena incorrecta')

    def test_rol_based_redirects(self):
        # Test for each role
        data = {
            'username': 'user1',
            'password': 'password1'
        }
        response = self.client.post(reverse('signin'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.client.logout()

        data = {
            'username': 'user2',
            'password': 'password2'
        }
        response = self.client.post(reverse('signin'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('menu filantropia'))
        self.client.logout()

        data = {
            'username': 'user3',
            'password': 'password3'
        }
        response = self.client.post(reverse('signin'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('bienestarUniversitario'))
        self.client.logout()

        data = {
            'username': 'user4',
            'password': 'password4'
        }
        response = self.client.post(reverse('signin'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('menuContabilidad'))
        self.client.logout()

        data = {
            'username': 'user5',
            'password': 'password5'
        }
        response = self.client.post(reverse('signin'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('menuBalanceAcademico'))
        self.client.logout()

        data = {
            'username': 'user6',
            'password': 'password6'
        }
        response = self.client.post(reverse('signin'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('crea'))
        self.client.logout()

    def test_invalid_rol(self):
        data = {
            'username': 'user7',
            'password': 'password7',
        }
        response = self.client.post(reverse('signin'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signin.html')
        self.assertContains(response, 'No puede entrear')
