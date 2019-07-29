from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Network, Address


# Relationship between ids:
# class NetworkSerializer(serializers.ModelSerializer):
# Relationship between hyperlinks (Relationships use HyperlinkedRelatedField, instead of PrimaryKeyRelatedField):
class NetworkSerializer(serializers.HyperlinkedModelSerializer):

    # The code below perform the associating between user and network
    owner = serializers.ReadOnlyField(source='owner.username')

    # The code below perform the associating between many address to one network
    addresses = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='address-detail')

    class Meta:
        model = Network
        fields = ['url', 'id', 'title', 'description', 'enabled', 'type', 'owner', 'addresses']


# Relationship between ids:
# class UserSerializer(serializers.ModelSerializer):
# Relationship between hyperlinks (Relationships use HyperlinkedRelatedField, instead of PrimaryKeyRelatedField):
class UserSerializer(serializers.HyperlinkedModelSerializer):

    # The code below perform the associating between user and network
    networks = serializers.PrimaryKeyRelatedField(many=True, queryset=Network.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'networks']


class AddressSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Address
        fields = ['url', 'id', 'ip', 'title', 'description']
