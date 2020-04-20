from rest_framework import permissions


class IsPublicIsCreation(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'create':
            return True
        else:
            if request.user.is_authenticated:
                return True
            else:
                return False


class IsPublicIsList(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        else:
            if request.user.is_authenticated:
                return True
            else:
                return False
