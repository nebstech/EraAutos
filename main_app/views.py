from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Car, ModificationLog, CarClub, UserProfile
from .serializers import CarSerializer, ModificationLogSerializer, CarClubSerializer, UserProfileSerializer, \
    UserSerializer
from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

# User Registration
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': response.data
        })


# User Login
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# User Verification
class VerifyUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = User.objects.get(username=request.user)  # Fetch user profile
        refresh = RefreshToken.for_user(request.user)  # Generate new refresh token
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        })


class Home(APIView):
    def get(self, request):
        data = {
            'message': "Welcome to our Django backend!",
            'status': "success"
        }
        return Response(data)


class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Car.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        print("Instance: ", instance)
        serializer = self.get_serializer(instance)

        cars_not_associated = Car.objects.exclude(id__in=[instance.id])
        cars_serializer = CarSerializer(cars_not_associated, many=True)

        return Response({
            'car': serializer.data,
            'cars_not_associated': cars_serializer.data
        })

    def perform_update(self, serializer):
        car = self.get_object()
        if car.user != self.request.user:
            raise PermissionDenied({"message": "You do not have permission to edit this car."})
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied({"message": "You do not have permission to delete this car."})
        instance.delete()


class ModificationLogList(generics.ListCreateAPIView):
    queryset = ModificationLog.objects.all()
    serializer_class = ModificationLogSerializer


class ModificationLogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ModificationLog.objects.all()
    serializer_class = ModificationLogSerializer
    lookup_field = 'id'


class UserProfileView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'id'


class CarClubListView(ListAPIView):
    queryset = CarClub.objects.all()
    serializer_class = CarClubSerializer
