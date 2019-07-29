# from django.urls import reverse
# from rest_framework import status
from rest_framework.test import APITestCase
# from .models import Network


class DummyTests(APITestCase):

    def test_dummy_test(self):
        print("----------- test_dummy_test ----------- ")
        self.assertTrue(True)

'''
class NetworkTests(APITestCase):
    def test_create_network(self):

        url = reverse('network-list')
        data = {'title': 'New Network'}
        response = self.client.post(url, data, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Network.objects.count(), 1)
        self.assertEqual(Network.objects.get().name, 'New Network')
'''