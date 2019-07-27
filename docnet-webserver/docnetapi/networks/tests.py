from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from docnetapi.networks.models import Network


class NetworkTests(APITestCase):

    def test_true(self):
        # To ensure test can run
        print("\n\n# -----test_true-----")
        self.assertTrue(True)

    def test_create_network(self):
        # Ensure we can create a new object.
        print("\n\n# -----test_create_network-----")

        url = reverse('network-list')
        data = {
            'title': 'New network title',
            'description': 'New network description'
        }
        response = self.client.post(url, data, format='json')
        # print(response) # to debug
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Network.objects.count(), 1)
        self.assertEqual(Network.objects.get().title, 'New network title')
