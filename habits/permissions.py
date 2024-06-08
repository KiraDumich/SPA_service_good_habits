from rest_framework.permissions import BasePermission


class Owner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False


class IsAdminUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        if self.request.user.is_superuser:
            return True
        return False
