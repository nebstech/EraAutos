from rest_framework import serializers
from .models import Car, ModificationLog, CarClub, UserProfile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Add a password field, make it write-only

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']  # Ensures the password is hashed correctly
        )
        return user

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

    def validate_model(self, value):
        if not isinstance(value, str):
            raise serializers.ValidationError("Model must be a valid string.")
        return value

    def validate_make(self, value):
        if not isinstance(value, str):
            raise serializers.ValidationError("Make must be a valid string.")
        return value

    def validate_year(self, value):
        if not isinstance(value, int):
            raise serializers.ValidationError("Year must be a valid integer.")
        return value

class ModificationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModificationLog
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'

class CarClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarClub
        fields = ['name', 'description', 'members']
