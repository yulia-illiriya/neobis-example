from django.urls import path
from .services import *
from .views import UserProfileAPIView, LogoutView


urlpatterns = [
    path('send-verification-code/', send_verification_code, name='send_verification_code'),
    path('verify-code/', verify_code, name="verify_code"),
    path('profile/', UserProfileAPIView.as_view(), name="profile"),
]