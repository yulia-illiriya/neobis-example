from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from django.views import View
from profile_user.services import send_verification_code, verify_code
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

from django.contrib.auth import authenticate, logout
from django.shortcuts import redirect

from .models import UserProfile
from .serializers import UserProfileSerializer
from .permissions import IsOwnerOrReadOnly


class SendVerificationCodeView(View):
    def post(self, request):
        return send_verification_code(request)
    

class VerifyCodeView(View):
    def post(self, request):
        return verify_code(request)
    

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user:
        refresh = RefreshToken.for_user(user)
        response_data = {'access_token': str(refresh.access_token)}
        return redirect('profile')  # Редирект на профиль пользователя
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    
class UserProfileDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self):
        user_profile = get_object_or_404(UserProfile, user=self.request.user)
        self.check_object_permissions(self.request, user_profile)
        return user_profile
    
class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_200_OK)