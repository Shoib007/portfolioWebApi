from rest_framework import serializers
from .models import projectDB

class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = projectDB
        exclude = ['id',]