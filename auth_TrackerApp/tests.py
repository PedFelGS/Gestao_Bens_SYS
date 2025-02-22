from django.test import TestCase
from django.urls import reverse

class AuthURLSTest(TestCase):
    def test_TrackerAPP_login_url_is_correct(self):
      login_url = reverse('auth_TrackerApp:login_view')
      self.assertEqual(login_url, '/auth/login/')
    
    def test_TrackerAPP_logout_url_is_correct(self):
        logout_url = reverse('auth_TrackerApp:logout_view')
        self.assertEqual(logout_url, '/auth/logout/')

    def test_TrackerAPP_register_url_is_correct(self):
        register_url = reverse('auth_TrackerApp:register_view')
        self.assertEqual(register_url, '/auth/register/')