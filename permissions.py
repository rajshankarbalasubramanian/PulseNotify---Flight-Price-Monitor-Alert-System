from rest_framework.permissions import BasePermission
from .models import UserProfile


class IsAdminUser(BasePermission):
    """Grants access only to users whose profile role is 'admin'."""

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        try:
            return request.user.profile.role == UserProfile.Role.ADMIN
        except UserProfile.DoesNotExist:
            return False
