from django.urls import path
from .views import SendVerificationCodeView, VerifyCodeView

urlpatterns = [
    path('verify-phone/', SendVerificationCodeView.as_view(), name='send_verification_code'),
    path('verify-code/', VerifyCodeView.as_view(), name="verify-code")
]