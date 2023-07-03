from django.contrib import admin
from profile_user.models import UserProfile, User

admin.site.register(User)
admin.site.register(UserProfile)
