from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from .models import Network, Address
from .serializers import NetworkSerializer, UserSerializer, AddressSerializer
from .permissions import IsOwnerOrReadOnly  # Custom permission, where any one can see, but only owner can edit


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


# The view below will return to root (http://localhost:8001/) the networks and users
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
            'users': reverse('user-list', request=request, format=format),
            'networks': reverse('network-list', request=request, format=format),
            'addresses': reverse('address-list', request=request, format=format)
        }
    )


# Class based views
class NetworkList(generics.ListCreateAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer

    # Only authenticated users are able to create, update and delete code networks.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # The code below perform the associating between user and network
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NetworkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer

    # Only authenticated users are able to create, update and delete code networks.
    # But any one can see
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Only authenticated users are able to create, update and delete code networks.
    # But, other authenticated users can see (from the custom permission IsOwnerOrReadOnly)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    # Only authenticated users are able to create, update and delete code networks.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AddressDetail(generics.RetrieveAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
