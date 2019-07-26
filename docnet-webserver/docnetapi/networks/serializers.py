from rest_framework import serializers
from docnetapi.networks.models import Network


class NetworkSerializer(serializers.HyperlinkedModelSerializer):

    # Fields created automatically:
    class Meta:
        model = Network
        fields = ['id', 'created', 'title', 'description', 'enabled']
