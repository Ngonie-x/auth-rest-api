from django.shortcuts import render
from . import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import HouseModel
from rest_framework import viewsets
from .serializers import HouseSerializer
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly



# Create your views here.


class HouseViewSet(viewsets.ModelViewSet):
    """House ViewSet"""
    
    serializer_class = HouseSerializer
    queryset = HouseModel.objects.all()
     #enables search by name and email
    filter_backends = (filters.SearchFilter,)
    search_fields = ('address', 'rent', 'rooms', 'property_choice', 'gender', 'space_type')
    permission_classes = (IsAuthenticatedOrReadOnly,)


    






