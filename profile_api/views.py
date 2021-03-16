from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from profile_api import serializers
from profile_api import models
from profile_api import permissions


class HelloApiView(APIView):
    """ Test APIView"""
    serializer_class = serializers.HelloSerializer

    name = 'Hello Api View'

    def get(self, request, format=None):
        """Returns list of APIView features """
        an_api_view = [
            'Uses rest api methods as functions (get, post, put , patch and delete)',
            'Is similar to django View',
            'Give you most of the control over logic',
            'is mapped to urls'
        ]
        return Response({'message': 'Hello World', 'an_apiview': an_api_view})

    def post(self, request, format=None):
        """ creating hello message """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Used to update model"""
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """Used to update model"""
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """Used to update model"""
        return Response({"method": "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """ Testing ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Returns list of features of ViewSet"""

        a_viewset = [
            'Uses actions [list, retrive, create, delete, update]',
            'Automatically maps urls to Router',
            'Create more functionality with less code'
        ]
        return Response({'message': 'Hi from view set', 'a_viewset': a_viewset})

    def create(self, request):
        """ Create a new message via ViewSet"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrive(self, request, pk=None):
        return Response({'method': request.method, 'data': request.data}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        return Response({'method': request.method, 'data': request.data}, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        return Response({'method': request.method, 'data': request.data}, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        return Response({'method': request.method, 'data': request.data}, status=status.HTTP_200_OK)


class UserProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfilePermission,)
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
