from django.shortcuts import render
from .models import Car
from .serializers import CarSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'id'

class Home(APIView):
    def get(self, request):
        data ={
            'message': "Welcome to our Django backend!",
            'status': "success"
        }
        return Response(data)