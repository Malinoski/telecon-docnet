from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Network


class NetworkSerializer(serializers.ModelSerializer):

    # The code below perform the associating between user and network
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Network
        fields = ['id', 'title', 'description', 'enabled', 'type', 'owner']


class UserSerializer(serializers.ModelSerializer):

    # The code below perform the associating between user and network
    networks = serializers.PrimaryKeyRelatedField(many=True, queryset=Network.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'networks']
