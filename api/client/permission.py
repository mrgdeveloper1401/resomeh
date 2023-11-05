from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
            
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True