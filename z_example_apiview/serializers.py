from rest_framework import serializers
from .models import Example1


class SerializerForApiView(serializers.ModelSerializer):
    class Meta:
        model = Example1
        fields = "__all__"
