from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    # Admin can write and read
    # Anybody can read only
    def has_permission(self, request, view):
        # Always allow GET HEAD OPTIONS 
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow all only admin
        return request.user.is_superuser
