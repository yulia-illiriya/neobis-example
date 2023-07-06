from django.db import models
from profile_user.managers import UserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _ 
from config import settings


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=255, unique=True)
    email = models.EmailField(_('email address'), null=True, blank=True)
    phone = models.CharField(_('phone number'), max_length=30, null=True, blank=True)
    name = models.CharField("Имя", max_length=500, null=True, blank=True)
    surname = models.CharField("Фамилия", max_length=500, null=True, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)

    is_verified_by_phone = models.BooleanField(_('verified'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        unique_together = ('username', 'email', 'phone')
        
        
class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    name = models.CharField("Имя", max_length=500)
    surname = models.CharField("Фамилия", max_length=500)
    phone = models.CharField(_('Номер телефона'), max_length=30, null=True, blank=True)
    is_verified = models.BooleanField(_('Статус верификации'), default=False)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
        

    def __str__(self):
        return f"{self.name} {self.surname}"
