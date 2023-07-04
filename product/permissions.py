from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsVerifiedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated and not user.is_verified:
            return request.method in SAFE_METHODS
        return True