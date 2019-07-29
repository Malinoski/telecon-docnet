from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from .models import Network


class NetworkTests(APITestCase):

    def setUp(self):

        # Create a user and collect the token
        self.user = User.objects.create_user(username='admin', email='admin@example.com', password='admin')
        token = Token.objects.create(user=self.user)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_dummy_test(self):

        print("\n\n----------- test_dummy_test ----------- ")
        self.assertTrue(True)

    def test_create_network(self):

        print("\n\n----------- test_create_network ----------- ")

        data = {
            "title": "New Network",
            "description": "A description"
        }

        url = reverse('network-list')
        # or
        # url = '/networks/'

        # response = self.client.post(reverse('network-list'), data, format='json')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Network.objects.count(), 1)

    def test_create_network_with_no_title(self):

        print("\n\n----------- test_create_network_with_no_title ----------- ")

        data = {
            "title"
            "description": "A description"
        }

        url = reverse('network-list')
        # or
        # url = '/networks/'

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Network.objects.count(), 0)
