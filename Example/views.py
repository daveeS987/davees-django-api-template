from rest_framework import generics
from .serializers import ExampleSerializer
from .models import Example


class ExampleList(generics.ListCreateAPIView):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer


class ExampleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer
