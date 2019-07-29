from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Network


# Relationship between ids:
# class NetworkSerializer(serializers.ModelSerializer):
# Relationship between hyperlinks (Relationships use HyperlinkedRelatedField, instead of PrimaryKeyRelatedField):
class NetworkSerializer(serializers.HyperlinkedModelSerializer):

    # The code below perform the associating between user and network
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Network
        fields = ['url', 'id', 'title', 'description', 'enabled', 'type', 'owner']


# Relationship between ids:
# class UserSerializer(serializers.ModelSerializer):
# Relationship between hyperlinks (Relationships use HyperlinkedRelatedField, instead of PrimaryKeyRelatedField):
class UserSerializer(serializers.HyperlinkedModelSerializer):

    # The code below perform the associating between user and network
    networks = serializers.PrimaryKeyRelatedField(many=True, queryset=Network.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'networks']
