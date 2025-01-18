from rest_framework import permissions


class IsModer(permissions.BasePermission):
    """
    Проверяет, является ли пользователь модератором.
    """

    message = "Модератор"

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moderator").exists()


class IsOwner(permissions.BasePermission):
    """
    Проверяет, является ли пользователь создателем объекта.
    """

    def has_object_permission(self, request, view, obj):

        if obj.owner == request.user:
            return True
        return False
