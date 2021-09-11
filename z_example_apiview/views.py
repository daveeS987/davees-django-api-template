from rest_framework import generics
from .serializers import SerializerForApiView
from .models import Example1


class Example1List(generics.ListCreateAPIView):
    queryset = Example1.objects.all()
    serializer_class = SerializerForApiView


class Example1Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Example1.objects.all()
    serializer_class = SerializerForApiView
