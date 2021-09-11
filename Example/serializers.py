from rest_framework import serializers
from .models import Example


class SerializerForApiView(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = "__all__"
