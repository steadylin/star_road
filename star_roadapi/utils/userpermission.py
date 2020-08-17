from rest_framework.permissions import BasePermission
from user.models import User


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        user_obj = User.objects.filter(username=user).first()
        if user_obj:
            is_vip = user_obj.is_vip
            print(is_vip)
            if is_vip == 1:
                print(is_vip)
                return True
            else:
                return False
        else:
            return False




