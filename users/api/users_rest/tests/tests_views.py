from http import client
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from users_rest.models import User, Foodie, Owner
import json

class TestViews(TestCase):

    def test_api_users_GET(self):
        client = Client()

        response = client.get(reverse('api_users'))

        self.assertEquals(response.status_code, 200)