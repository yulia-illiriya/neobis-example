from django.urls import path
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_yasg.inspectors import SwaggerAutoSchema

schema_view = get_schema_view(
    openapi.Info(
        title="Marketplace",
        default_version='v1',
        description="API documentation",
        terms_of_service="none",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[],
    authentication_classes=[],
)


class CustomAutoSchema(SwaggerAutoSchema):
    def get_tags(self, operation_keys=None):
        if self.method == 'POST' and 'users' in self.path:
            return ['Users']
        if self.method in ['GET', 'PUT', 'PATCH', 'DELETE']:
            if 'auth' in self.path:
                return ['Authentication']
            if 'product' in self.path:
                return ['Categories']
        return []


urlpatterns = [    
    path('swagger/', schema_view.with_ui('swagger'), name='swagger'),
    path('redoc/', schema_view.with_ui('redoc'), name='redoc'),    
]