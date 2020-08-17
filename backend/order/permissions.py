from rest_framework import permissions


class ChangeOrderStatusPermission(permissions.BasePermission):

    message = "You do not have permission to change order status"

    def has_object_permission(self, request, view, obj):
        if not request.user.is_superuser:
            if request.method in permissions.SAFE_METHODS:
                return True
            changed_status = request.data.get("status", None)
            return obj.status == "P" and changed_status == "C" if changed_status else True
        return True
