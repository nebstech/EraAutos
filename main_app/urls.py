from django.urls import path
from .views import Home, CarList, CarDetail, ModificationLogList, ModificationLogDetail, CarClubListView, CreateUserView, LoginView, VerifyUserView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('users/register/', CreateUserView.as_view(), name='register'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/token/refresh', VerifyUserView.as_view(), name='token-refresh'),
    path('car/', CarList.as_view(), name='car-list'),
    path('car/<int:id>', CarDetail.as_view(), name='car-details'),
    path('modifications/', ModificationLogList.as_view(), name='modification-list'),
    path('modifications/<int:id>', ModificationLogDetail.as_view(), name='modification-detail'),
    path('user-clubs/', CarClubListView.as_view(), name='user-car-clubs'),
]
