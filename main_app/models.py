from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username
# Create your models here.
class Car(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, related_name='cars')
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

class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

