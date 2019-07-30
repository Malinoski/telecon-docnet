from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Network, Address


class NetworkSerializer(serializers.HyperlinkedModelSerializer):

    # The code below perform the associating between user and network
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Network
        fields = ['url', 'id', 'title', 'cidr', 'description', 'enabled', 'type', 'owner']


class UserSerializer(serializers.HyperlinkedModelSerializer):

    # The code below perform the associating between user and network
    networks = serializers.PrimaryKeyRelatedField(many=True, queryset=Network.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'networks']


class AddressSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Address
        fields = ['id', 'url', 'ip', 'title', 'description', 'network', 'owner']
