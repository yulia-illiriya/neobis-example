from django.shortcuts import render
from django.views import View
from profile_user.services import send_verification_code, verify_code
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import UserProfile
from .serializers import UserProfileSerializer

class SendVerificationCodeView(View):
    def post(self, request):
        return send_verification_code(request)
    
class VerifyCodeView(View):
    def post(self, request):
        return verify_code(request)
    

class UserProfileDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        return get_object_or_404(UserProfile, user=user)

