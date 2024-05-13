from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.user.username
# Create your models here.
class Car(models.Model):
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    year = models.IntegerField(
        validators=[
            MinValueValidator(1800),
            MaxValueValidator(2020)
        ]
    )

    def __str__(self):
        return f'{self.model}, {self.make} ({self.year})'

