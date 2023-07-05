from django.dispatch import receiver
from djoser.signals import user_registered
from django.db.models.signals import post_save

from profile_user.models import UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()

profile_created = False

@receiver(user_registered, dispatch_uid="create_profile")
def create_profile(sender, user, request, **kwargs):
    """Создаём профиль пользователя при регистрации"""
    data = request.data

    global profile_created

    if not profile_created:
        UserProfile.objects.create(
            user=user,
            name=data.get("name", ""),
            surname=data.get("surname", ""),
            phone=data.get("phone", "")
        )
        profile_created = True
        
    
# @receiver(post_save, sender=User, dispatch_uid="create_user_profile")
# def create_user_profile(sender, instance, created, **kwargs):
#     global profile_created

#     if created and not profile_created:
#         profile = UserProfile.objects.create(user=instance)
#         if hasattr(instance, 'name'):
#             profile.name = instance.name
#         if hasattr(instance, 'surname'):
#             profile.surname = instance.surname
#         if hasattr(instance, 'phone'):
#             profile.phone = instance.phone
#         profile.save()
        
