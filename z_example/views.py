from rest_framework import generics
from .serializers import SerializerForApiView
from .models import Example


class ExampleList(generics.ListCreateAPIView):
    queryset = Example.objects.all()
    serializer_class = SerializerForApiView


class ExampleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Example.objects.all()
    serializer_class = SerializerForApiView
