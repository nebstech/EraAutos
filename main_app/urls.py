from django.urls import path
from .views import Home, CarList, CarDetail

urlpatterns = [
    path(''. Home.as_view(), name='home')
    path('car/', CarList.as_view(), name='car-list')
    path('car/<int:id>', CarDetail.as_view(), name='car-details')
]