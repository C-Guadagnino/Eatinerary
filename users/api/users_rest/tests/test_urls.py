from django.test import SimpleTestCase
from django.test import TestCase
from django.urls import reverse, resolve
from users_rest.views import api_users, api_user_token, api_get_specific_user, api_list_users

 # python manage.py test users_rest
class TestUrls(SimpleTestCase):

    def test_users_url_resolves(self):
        url = reverse('api_users')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, api_users)

    def test_specific_users_url_resolves(self):
        url = reverse('api_users')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, api_users)

    def test_list_users_resolves(self):
        url = reverse('api_list_users')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, api_list_users)
        
    def test_token_resolves(self):
        url = reverse('api_user_token')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, api_user_token)