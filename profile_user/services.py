from config import settings
from django.http import JsonResponse
from django.shortcuts import redirect
from twilio.rest import Client
from django.contrib.auth import get_user_model

User = get_user_model()

def send_verification_code(request):
    phone_number = request.POST.get('phone_number')

    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    verification = client.verify \
        .services(settings.TWILIO_VERIFY_SERVICE_SID) \
        .verifications \
        .create(to=phone_number, channel='sms')

    if verification.status == 'pending':
        
        request.session['phone_number'] = phone_number
        return redirect('verify_code')  
    else:
        return JsonResponse({'status': 'error', 'message': 'Failed to send verification code'})

    

def verify_code(request):
    phone_number = request.session.get('phone_number')
    verification_code = request.POST.get('verification_code')

    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    try:
        verification_check = client.verify \
            .services(settings.TWILIO_VERIFY_SERVICE_SID) \
            .verification_checks \
            .create(to=phone_number, code=verification_code)

        if verification_check.status == 'approved':
            
            user = request.user
            user.is_verified_by_phone = True
            user.save()
            return JsonResponse({'status': 'success', 'message': 'Verification code is valid'})
        else:
            # Код верификации неверен
            return JsonResponse({'status': 'error', 'message': 'Invalid verification code'})
    except Exception as e:
        # Ошибка при проверке кода верификации
        return JsonResponse({'status': 'error', 'message': str(e)})
    
    
def verify_user(request):
    user = request.user

    if user.is_verified == False:
        return redirect('send_verification_code')