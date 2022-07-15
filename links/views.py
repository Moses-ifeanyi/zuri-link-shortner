from django.shortcuts import render
from django.db import models 
import datetime
from django.utils import timezone

from .models import Link
from links.serializers import LinkSerializer
from rest_framework import generics, serializers, status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request


# Create your views here.
class PostListApi(generics.ListCreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostCreateApi(generics.CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostUpdateApi(generics.UpdateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostDeleteApi(generics.DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class ActiveLinkView(APIView):
    """
    Returns a list of all active (publicly accessible) links
    """
    def get(self, request):
        """ 
        Invoked whenever a HTTP GET Request is made to this view
        """
        qs = Link.objects.filter(active=True)
        data = serializers.Serializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    
class RecentLinkView(APIView):
    """
    Returns a list of recently created active links
    """
    def get(self, request):
        """ 
        Invoked whenever a HTTP GET Request is made to this view
        """
        seven_days_ago = timezone.now() - datetime.timedelta(days=7)
        qs = Link.objects.filter(created_date__gte=seven_days_ago)
        data = serializers.Serializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)