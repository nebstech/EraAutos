from django.shortcuts import render
from .models import Car
from .serializers import CarSerializer
from rest_framework import generics

# Create your views here.

class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'id'