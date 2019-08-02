from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Network, Address
from .serializers import NetworkSerializer, UserSerializer, AddressSerializer
from .permissions import IsOwner  # Custom permissions

# Can be useful in future
# from .permissions import IsOwnerOrReadOnly,


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class NetworkView(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    # Can be useful in future:
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # This rewrites the get function to return elements only from their owner
    def get_queryset(self):
        user = self.request.user
        return Network.objects.filter(owner=user).order_by('id')


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AddressView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    # Can be useful in future:
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):

        # Check if has the parameter networkId.
        # Case yes, the filter act, like http://127.0.0.1:8001/addresses/?networkId=10,
        # case not, the filter is not required, like
        # edit (PUT http://127.0.0.1:8001/addresses/20/)
        # delete (DELETE http://127.0.0.1:8001/addresses/20/)
        # get one (GET http://127.0.0.1:8001/addresses/20/)
        network_id = self.request.query_params.get('networkId', None)

        # In both cases, any request act only on the address owner
        user = self.request.user

        if network_id is not None:
            return Address.objects.filter(owner=user, network=network_id)
        return Address.objects.filter(owner=user)
