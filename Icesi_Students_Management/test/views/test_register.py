from django.test import TestCase, Client
from django.urls import reverse
from Icesi_Students_Management.models import User


# Test for register view
class RegisterTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test', password='test')
        self.user.save()

    def test_register_successful(self):
        response = self.client.post(reverse('signup'), {
            'username': 'test2',
            'password1': 'test2',
            'password2': 'test2',
            'name': 'test2',
            'lastName': 'test2',
            'email': 'test2@test2',
            'phoneNumber': '123456789'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('signin'))

    def test_register_password_mismatch(self):
        response = self.client.post(reverse('signup'), {
            'username': 'test3',
            'password1': 'test3',
            'password2': 'mismatch',
            'name': 'test3',
            'lastName': 'test3',
            'email': 'test3@test3',
            'phoneNumber': '987654321'
        })
        self.assertEqual(response.status_code, 200)  # Registration form should be rendered again
        self.assertContains(response, 'Contraseñas son distintas')

    def test_register_missing_fields(self):
        response = self.client.post(reverse('signup'), {
            'username': 'test4',
            'password1': 'test4',
            'password2': 'test4',
            'name': '',
            'lastName': '',
            'email': '',
            'phoneNumber': ''
        })
        self.assertEqual(response.status_code, 200)  # Registration form should be rendered again
        self.assertContains(response, 'Todos los campos son requeridos')

    def test_register_existing_user(self):
        response = self.client.post(reverse('signup'), {
            'username': 'test',
            'password1': 'test',
            'password2': 'test',
            'name': 'test',
            'lastName': 'test',
            'email': 'test@test',
            'phoneNumber': '987654321'
        })
        self.assertEqual(response.status_code, 200)  # Registration form should be rendered again
        self.assertContains(response, 'Usuario ya existe')