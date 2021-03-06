from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from rest_framework.request import Request

from ..models import Network
from ..serializers import NetworkSerializer

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


class GetAllNetworksTest(APITestCase):
    """ Test module for GET all networks API """

    def setUp(self):

        # Create a user and collect the token
        authenticate(self)

        # Create some networks in test db
        Network.objects.create(title='My netwotk 01', description="My description 01", owner=self.user)
        Network.objects.create(title='My netwotk 02', description="My description 02", owner=self.user)

    def test_get_all_networks(self):

        # get API response
        response = self.client.get(reverse('network-list'))

        # get data from db
        networks = Network.objects.all()
        serializer = NetworkSerializer(networks, many=True, context=get_serializer_context())

        # Some debugs:
        # print("\n---DEBUG--\n");
        # print("\n---RESPONSE--\n");
        # print(response.data['results']);
        # print("\n---SERIALIZER--\n");
        # print(serializer.data);

        # Check if is equals the data from http request (response.data) and db (serializer.data))
        self.assertEqual(response.data['results'], serializer.data)

        # Check if the http request was executed ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleNetworkTest(APITestCase):
    """ Test module for GET single network API """

    def setUp(self):

        # Create a user and collect the token
        authenticate(self)

        # Create some networks
        self.network01 = Network.objects.create(title='My netwotk 01', cidr="10.0.0.0", description="My description 01", owner=self.user)
        self.network02 = Network.objects.create(title='My netwotk 02', cidr="10.0.0.1", description="My description 02", owner=self.user)

    def test_get_valid_single_network(self):

        # Note: The reverse(..) function below means to get an url like '/networks/1/'
        response = self.client.get(reverse('network-detail', kwargs={'pk': self.network01.pk}))

        network = Network.objects.get(pk=self.network01.pk);
        serializer = NetworkSerializer(network, context=get_serializer_context())

        # Some debugs:
        # print("\n---DEBUG");
        # print("\n---RESPONSE");
        # print(response.data);
        # print("\n---SERIALIZER");
        # print(serializer.data);

        # Check if is equals the data from http request (response.data) and db (serializer.data))
        self.assertEqual(response.data, serializer.data)

        # Check if the http request was executed ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_network(self):

        response = self.client.get(reverse('network-detail', kwargs={'pk': 99}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_valid_single_network_filter_by_cidr(self):
        response = self.client.get('/networks/?part_cidr=' + str(self.network01.cidr));
        self.assertTrue(response.data['count'], 1)


class CreateNewNetworkTest(APITestCase):
    """ Test module for inserting a new network """

    def setUp(self):

        # Create a user and collect the token
        authenticate(self)

        self.valid_network = {
            'title': 'My network',
            'cidr': 'My CIDR',
            'description': 'My description'
        }
        self.invalid_network = {
            'title': 'My network',
            # 'cidr': 'My CIDR',
            'description': 'My description'
        }

    def test_create_valid_network(self):

        response = self.client.post(reverse('network-list'), data=json.dumps(self.valid_network), content_type='application/json')

        # print("\n------ MY DEBUG test_create_valid_network");
        # print(response)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_network(self):

        response = self.client.post(reverse('network-list'), data=json.dumps(self.invalid_network), content_type='application/json')

        # print("\n------ MY DEBUG test_create_valid_network");
        # print(response)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateNetworkTest(APITestCase):
    """ Test module for updating an existing network record """

    def setUp(self):

        # Create a user and collect the token
        authenticate(self)

        # Create one network
        self.network01 = Network.objects.create(title='My netwotk 01', description="My description 01", owner=self.user)

        # Define some data
        self.valid_update_network_data = {
            'title': 'My new title',
            'cidr': 'My new CIDR',
            'description': 'My new description'
        }
        self.invalid_update_network_data = {
            'title': 'My new title',
            #'cidr': 'My new CIDR',
            'description': 'My new description'
        }

    def test_valid_update_network(self):
        response = self.client.put(
            reverse('network-detail', kwargs={'pk': self.network01.pk}),
            data=json.dumps(self.valid_update_network_data),
            content_type='application/json')

        # print("\n------ MY DEBUG test_valid_update_network");
        # print(response.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_netowrk(self):
        response = self.client.put(
            reverse('network-detail', kwargs={'pk': self.network01.pk}),
            data=json.dumps(self.invalid_update_network_data),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteNetworkTest(APITestCase):
    """ Test module for deleting an existing network record """

    def setUp(self):

        # Create a user and collect the token
        authenticate(self)

        # Create some networks
        self.network01 = Network.objects.create(title='My network 01', description="My description 01", owner=self.user)
        self.network02 = Network.objects.create(title='My network 02', description="My description 02", owner=self.user)

    def test_valid_delete_network(self):
        response = self.client.delete(reverse('network-detail', kwargs={'pk': self.network01.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_network(self):
        response = self.client.delete(reverse('network-detail', kwargs={'pk': 99}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
