from rest_framework import serializers
from .models import ModelForApiView


class SerializerForApiView(serializers.ModelSerializer):
    class Meta:
        model = ModelForApiView
        fields = "__all__"
