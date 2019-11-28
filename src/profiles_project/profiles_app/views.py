from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test API View"""
    def get(self, request ,format=None):
        """Returns a list of APIView Features"""
        an_apiview = ['Uses HTTP methods as function (get,post,patch,ut,delete)',
        'It is similar to a traditional django view',
        'Gives you most control over your logic',
        'Is mapped manually to URLs']

        return Response({'message':'Hello!','an_apiview':an_apiview})
