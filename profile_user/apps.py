from django.apps import AppConfig


class ProfileUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profile_user'

    def ready(self):
        from profile_user import signals