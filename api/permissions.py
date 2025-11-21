from rest_framework import permissions


class IsSuperuser(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsSuperuserOrReadonly(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and
            request.user.is_superuser
        )

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user == obj.user
        )

class IsOwnerProduct(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.product.user
