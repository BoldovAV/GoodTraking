from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return request.method in ['GET', 'PUT', 'PATCH', 'DELETE']
        return False
