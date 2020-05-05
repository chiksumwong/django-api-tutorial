from rest_framework import permissions

# View Action:
# list
# create
# retrieve
# update
# partial_update
# destroy


class IsPublicCreate(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        else:
            if view.action == 'create':
                return True
            else:
                return False


class IsPublicList(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        else:
            if view.action == 'list':
                return True
            else:
                return False


class IsOwnerRetrieveIsAdminList(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            # Instance must have an attribute named `owner`.
            if obj.owner == request.user:
                if view.action == 'list':
                    return True
                else:
                    return False
        else:
            if view.action == 'retrieve':
                return True
            else:
                return False
