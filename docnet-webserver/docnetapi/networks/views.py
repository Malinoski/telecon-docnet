from rest_framework import viewsets
from .models import Network
from .serializers import NetworkSerializer


class NetworkViewSet(viewsets.ModelViewSet):

    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
