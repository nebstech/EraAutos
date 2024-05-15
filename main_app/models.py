from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

MODIFICATION_CATEGORIES = (
    ('P', 'Performance'),
    ('A', 'Aesthetic'),
    ('T', 'Technology'),
    ('S', 'Safety'),
    ('O', 'Other')
)


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
    modifications = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='car_images/', null=True, blank=True)

    def __str__(self):
        return f'{self.model}, {self.make} ({self.year})'


class ModificationLog(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='modification_logs')
    category = models.CharField(
        max_length=1,
        choices=MODIFICATION_CATEGORIES,
        default=MODIFICATION_CATEGORIES[0][0]
    )
    description = models.TextField()
    cost = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.get_category_display()} for {self.car}"

class CarClub(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(UserProfile, related_name='car_clubs')

    def __str__(self):
        return f'{self.name}, {self.members.name}'


class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
