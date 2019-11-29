from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from . import models
from rest_framework import status


class HelloAPIView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request ,format=None):
        """Returns a list of APIView Features"""
        an_apiview = ['Uses HTTP methods as function (get,post,patch,ut,delete)',
        'It is similar to a traditional django view',
        'Gives you most control over your logic',
        'Is mapped manually to URLs']

        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self ,request):
            """Create a hello message with our name"""
            serializer = serializers.HelloSerializer(data=request.data)

            if serializer.is_valid():
                name = serializer.data.get('name')
                message = 'Hello {0}'.format(name)
                return Response({'message':message})
            else:
                return Response(
                serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self , request , pk=None):
                """Handles updating an object"""
                return Response({'method':'put'})

    def patch(self , request , pk=None):
                """Only Updates fields provided in the object [Partial Updation]"""
                return Response({'method':'patch'})

    def delete(self , request , pk=None):
                """Deletes and Object"""
                return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self , request):
        """Return a Hello message"""
        a_viewset = [
        'Uses actions (list  create , update , partial_update)',
        'Automatically maps to URLs using Routers',
        'Provides more functionality with less code'
        ]

        return Response({'message':'Hello!','a_viewset':a_viewset})

    def create(self , request):
        """Create a new Hello message"""

        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(
            serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self , request , pk=None):
        """Handles getting an Object by its ID"""
        return Response({'http_method':'GET'})

    def update(self , request , pk=None):
        """Handles updating an Object"""
        return Response({'http_method':'PUT'})

    def partial_update(self , request , pk=None):
        """Handles Updating part of an Object"""
        return Response({'http_method':'PATCH'})

    def destroy(self , request , pk=None):
        """Handles removing an Object"""
        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
        """Handles creating and updating profiles"""
        serializer_class = serializers.UserProfileSerializer
        queryset = models.UserProfile.object.all()
