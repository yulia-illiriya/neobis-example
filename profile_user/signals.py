from django.dispatch import receiver
from djoser.signals import user_registered
from django.db.models.signals import post_save

from profile_user.models import UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(user_registered, dispatch_uid="create_profile")
def create_profile(sender, user, request, **kwargs):
    """Создаём профиль пользователя при регистрации"""
    data = request.data

    UserProfile.objects.create(
        user=user,
        name=data.get("name", ""),
        surname=data.get("surname", ""),
        phone=data.get("phone", "")
    )
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(
            user=instance,
            name=instance.name,
            surname=instance.surname,
            phone=instance.phone
        )