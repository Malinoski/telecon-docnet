from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Network, Address
from .serializers import NetworkSerializer, UserSerializer, AddressSerializer
from .permissions import IsOwnerOrReadOnly  # Custom permission, where any one can see, but only the owner can edit


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class NetworkView(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AddressView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):

        # Optionally restricts the returned purchases to a given network id,
        # by filtering against a `networkId` query parameter in the URL.

        queryset = Address.objects.all()
        networkId = self.request.query_params.get('networkId', None)
        if networkId is not None:
            queryset = queryset.filter(network=networkId)
        return queryset
