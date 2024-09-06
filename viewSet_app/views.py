from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.



class detial_viewset(viewsets.ModelViewSet):
    queryset=detail.objects.all()
    serializer_class=detailserializers


class single_detail_viewset(viewsets.ModelViewSet):
    queryset=detail.objects.all()
    serializer_class=detailserializers
