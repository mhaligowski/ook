from django.utils import unittest
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class ProfilesTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_register_user(self):
        # assert that there is no such user
        self.assertEquals(0, len(User.objects.filter(email = 'test1@emample.com')))
        
        # prepare test data
        user_form_data = {
            'email': 'test1@example.com',
            'password1': 'passw0rd',
            'password2': 'passw0rd'
        }
        
        # get url
        url = reverse('userena_signup')
        
        response = self.client.post(url, user_form_data)
        
        # assert that the response is 200 (OK)
        self.assertEquals(200, response.status_code)
        
        # asser that the user is created
        self.assertIsNotNone(User.objects.get(email = 'test1@example.com'))