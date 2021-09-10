from rest_framework import generics
from .serializers import SerializerForApiView
from .models import ModelForApiView


class ExampleList(generics.ListCreateAPIView):
    queryset = ModelForApiView.objects.all()
    serializer_class = SerializerForApiView


class ExampleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ModelForApiView.objects.all()
    serializer_class = SerializerForApiView
