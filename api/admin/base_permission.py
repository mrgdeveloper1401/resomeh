from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_superuser:
            return True
        return False
    