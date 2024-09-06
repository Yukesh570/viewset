from rest_framework import serializers
from .models import *

class detailserializers(serializers.ModelSerializer):
    class Meta:
        model=detail
        fields='__all__'