from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from .models import Network
from .serializers import NetworkSerializer
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly  # Custom permission, where any one can see, but only owner can edit


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