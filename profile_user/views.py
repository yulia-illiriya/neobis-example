from django.shortcuts import render
from django.views import View
from profile_user.services import send_verification_code, verify_code

class SendVerificationCodeView(View):
    def post(self, request):
        return send_verification_code(request)
    
class VerifyCodeView(View):
    def post(self, request):
        return verify_code(request)

