"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as swagger_urls
from djoser import views as djoser_views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/users/', djoser_views.UserViewSet.as_view({'post': 'create'}), name='user_create'),  # Регистрация пользователя
    path('auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),  # Обновление токена
    path('product/', include('product.urls')),
    path('profile/', include('profile_user.urls'))
]

urlpatterns += swagger_urls


