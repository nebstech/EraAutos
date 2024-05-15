from django.contrib import admin
from .models import Car, UserProfile, Comment, ModificationLog, CarClub

# Register your models here.

admin.site.register(Car)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(ModificationLog)
admin.site.register(CarClub)
