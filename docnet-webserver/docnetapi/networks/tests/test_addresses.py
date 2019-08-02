from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from rest_framework.request import Request

from ..models import Network, Address
from ..serializers import AddressSerializer, NetworkSerializer

import json


def get_serializer_context():
    factory = APIRequestFactory()
    request = factory.get('/')
    serializer_context = {
        'request': Request(request),
    }
    return serializer_context;


def authenticate(self):
    self.user = User.objects.create_user(username='user00', email='user00@example.com', password='user00')
    self.token = Token.objects.create(user=self.user)
    self.client = APIClient()
    self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)


class GetAddressesTest(APITestCase):
    """ Test module for GET address API """

    def setUp(self):

        # Create a user and collect the token
        authenticate(self)

        # Create two networks
        self.network01 = Network.objects.create(title='My network 01', description="My description", owner=self.user)
        self.network02 = Network.objects.create(title='My network 02', description="My description", owner=self.user)

        # Add 2 addresses to network01
        self.address01 = Address.objects.create(title='My address 01', description="My description", owner=self.user, network=self.network01)
        self.address02 = Address.objects.create(title='My address 02', description="My description", owner=self.user, network=self.network01)

        # Add 1 address to network02
        self.address03 = Address.objects.create(title='My address 03', description="My description", owner=self.user, network=self.network02)

    def test_get_all_address_from_specific_network(self):

        # Do not work. Something is wrong ...
        # response = self.client.get(reverse('address-list'), kwargs={'networkId': self.network01.id});
        # Alternative:
        response = self.client.get('/addresses/?networkId='+str(self.network01.id));

        # print("DEBUG test_get_two_address_from_network01")
        # print(response.data)

        # The network01 has only 2 addresses (address01, address02)
        self.assertTrue(response.data['count'], 2)

    def test_get_all_address_from_all_networks(self):

        # get API response
        response = self.client.get(reverse('address-list'))

        # print("DEBUG test_get_all_address_from_all_networks")
        # print(response.data)

        self.assertTrue(response.data['count'], 3)

    def test_get_single_address(self):

        # Below do not work. Something is wrong ...
        # response = self.client.get(reverse('address-detail'), kwargs={'pk': self.address02.pk})
        # Alternative
        response = self.client.get('/addresses/2/')

        # print("DEBUG test_get_single_address")
        # print(response.data)

        address = Address.objects.get(pk=self.address02.pk)
        serializer = AddressSerializer(address, context=get_serializer_context())

        # Check if is equals the data from http request (response.data) and db (serializer.data))
        self.assertEqual(response.data, serializer.data)

        # Check if the http request was executed ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateAddressTest(APITestCase):
    """ Test module for inserting """

    def setUp(self):

        # Create a user and collect the token
        authenticate(self)

        # Create one network
        self.network01 = Network.objects.create(title='My network 01', description="My description", owner=self.user)

        # We need to serialize the network, because the network model DO NOT HAVE the url field (we will use in valid_data)
        serializer = NetworkSerializer(self.network01, context=get_serializer_context())
        network_url = serializer.data['url'];

        # print("DEBUG")
        # print(serializer.data['url'])

        self.valid_data = {
            'ip': 'My address!',
            'title': 'My address',
            'description': 'My description',
            'network': network_url
        }
        self.invalid_data = {
            'ip': 'My address!',
            'title': 'My address',
            'description': 'My description',
            # 'network': network_url
        }

    def test_create_valid_address(self):

        response = self.client.post(reverse('address-list'), data=json.dumps(self.valid_data), content_type='application/json')

        # print("\nDEBUG test_create_valid_address");
        # print(response.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_address(self):

        response = self.client.post(reverse('address-list'), data=json.dumps(self.invalid_data), content_type='application/json')

        # print("\nDEBUG test_create_invalid_address");
        # print(response)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateAddressTest(APITestCase):
    """ Test module for updating """

    def setUp(self):

        # Create a user and collect the token
        authenticate(self)

        # Create an address (but we need a network)
        self.network01 = Network.objects.create(title='My network 01', description="My description", owner=self.user)
        self.address01 = Address.objects.create(
            title='My address 01', description="My description", owner=self.user, network=self.network01)

        # We need to serialize the network,
        # because the network model DO NOT HAVE the url field (we will use in valid_data)
        serializer = NetworkSerializer(self.network01, context=get_serializer_context())
        network_url = serializer.data['url'];

        # Define some data
        self.valid_data = {
            'ip': 'My address',
            'title': 'My address',
            'description': 'My description',
            'network': network_url
        }
        self.invalid_data = {
            'title': 'My new title',
            #'cidr': 'My new CIDR',
            'description': 'My new description'
        }

    def test_valid_update_address(self):

        response = self.client.put(
            reverse('address-detail', kwargs={'pk': self.address01.pk}),
            data=json.dumps(self.valid_data), content_type='application/json')

        # print("\nDEBUG test_valid_update_address");
        # print(response.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_network(self):
        response = self.client.put(
            reverse('address-detail', kwargs={'pk': self.network01.pk}),
            data=json.dumps(self.invalid_data),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteAddressTest(APITestCase):
    """ Test module for deleting  """

    def setUp(self):

        # Create a user and collect the token
        authenticate(self)

        # Create an address (but we need a network)
        self.network01 = Network.objects.create(title='My network 01', description="My description", owner=self.user)
        self.address01 = Address.objects.create(
            title='My address 01', description="My description", owner=self.user, network=self.network01)

    def test_valid_delete_address(self):
        response = self.client.delete(reverse('address-detail', kwargs={'pk': self.address01.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_address(self):
        response = self.client.delete(reverse('address-detail', kwargs={'pk': 99}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
