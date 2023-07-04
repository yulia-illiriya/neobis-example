from django.urls import path
from .services import *
from .views import UserProfileDetailAPIView


urlpatterns = [
    path('send-verification-code/', send_verification_code, name='send_verification_code'),
    path('verify-code/', verify_code, name="verify_code"),
    path('verify-user/', verify_user, name="verify_user"),
    path('profile/', UserProfileDetailAPIView.as_view(), name="profile")
]