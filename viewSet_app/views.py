from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import FilterSet
from .task import test_func
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

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

    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

    queryset=detail.objects.all()
    serializer_class=detailserializers
    search_fields = ['name', 'email']  #  in url /?search=yukesh
    ordering_fields = ['name', 'country']  #  in url /?ordering=name
    filterset_class=detailFilter
    authentication_classes = [TokenAuthentication]  # or any other authentication class

    permission_classes = [IsAuthenticated]
class single_detail_viewset(viewsets.ModelViewSet):

    queryset=detail.objects.all()
    serializer_class=detailserializers
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)


def test(request):
    test=test_func.apply_async().get(timeout=10)
    return HttpResponse(test)


