from django.core import management
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils import unittest
from django.test.client import Client

class ProfilesTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        management.call_command('check_permissions')
        
    def test_register_user(self):
        EXPECTED_EMAIL = 'test1@example.com'
        
        # assert that there is no such user
        self.assertEquals(0, len(User.objects.filter(email = EXPECTED_EMAIL)))
        
        # prepare test data
        user_form_data = {
            'email': EXPECTED_EMAIL,
            'password1': 'passw0rd',
            'password2': 'passw0rd'
        }
        
        # get url
        url = reverse('userena_signup')
        
        response = self.client.post(url, user_form_data)
        
        # assert that the response is 200 (OK)
        self.assertEquals(302, response.status_code)
        
        # asser that the user is created
        self.assertIsNotNone(User.objects.get(email = EXPECTED_EMAIL))
        
    def test_default_user_permissions(self):
        EXPECTED_EMAIL = 'test1@example.com'

        # assert that there is no such user
        self.assertEqual(0, len(User.objects.filter(email = EXPECTED_EMAIL)))
