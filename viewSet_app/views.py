from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import FilterSet

# Create your views here.



class detial_viewset(viewsets.ModelViewSet):
    class detailFilter(FilterSet):
        class Meta:
            model=detail    
            fields={
                'name':['exact','contains'],
                'address':['exact','contains'],
                'email':['exact','contains'],
                'country':['exact','contains'],
                'degree':['exact','contains'],
                'age':['exact'],

            }

    filterset_class=detailFilter
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

    queryset=detail.objects.all()
    serializer_class=detailserializers
    search_fields = ['name', 'email']  # Allows search for name or email via query params
    ordering_fields = ['name', 'country']  # You can order by name and country


class single_detail_viewset(viewsets.ModelViewSet):

    queryset=detail.objects.all()
    serializer_class=detailserializers
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
