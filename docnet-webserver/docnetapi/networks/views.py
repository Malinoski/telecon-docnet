# from django.http import HttpResponse, JsonResponse, Http404
# from django.views.decorators.csrf import csrf_exempt

# from rest_framework.parsers import JSONParser
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import mixins
from rest_framework import generics

from .models import Network
from .serializers import NetworkSerializer

'''
@csrf_exempt
def network_list(request):
    """
    List all code networks, or create a new network.
    """
    if request.method == 'GET':
        networks = Network.objects.all()
        serializer = NetworkSerializer(networks, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NetworkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def network_detail(request, pk):
    """
    Retrieve, update or delete a code network.
    """
    try:
        network = Network.objects.get(pk=pk)
    except Network.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = NetworkSerializer(network)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = NetworkSerializer(network, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        network.delete()
        return HttpResponse(status=204)
'''

'''
# Function based views
@api_view(['GET', 'POST'])
def network_list(request, format=None):  # Allow to set format (like a json)in a url
    """
    List all code networks, or create a new network.
    """
    if request.method == 'GET':
        networks = Network.objects.all()
        serializer = NetworkSerializer(networks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NetworkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def network_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code network.
    """
    try:
        network = Network.objects.get(pk=pk)
    except Network.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NetworkSerializer(network)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = NetworkSerializer(network, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        network.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

'''
# Class based views (detailed code)
class NetworkList(APIView):
    """
    List all networks, or create a new one.
    """
    def get(self, request, format=None):
        networks = Network.objects.all()
        serializer = NetworkSerializer(networks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NetworkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NetworkDetail(APIView):
    """
    Retrieve, update or delete a network instance.
    """
    def get_object(self, pk):
        try:
            return Network.objects.get(pk=pk)
        except Network.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        network = self.get_object(pk)
        serializer = NetworkSerializer(network)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        network = self.get_object(pk)
        serializer = NetworkSerializer(network, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        network = self.get_object(pk)
        network.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

'''
# Class based views (More compact) 
class NetworkList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NetworkDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
'''


# Class based views (Even more compact than before)
class NetworkList(generics.ListCreateAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer


class NetworkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
