from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication
from rest_framework_jwt.authentication import jwt_decode_handler
from rest_framework import exceptions
class MyAuthentication(BaseJSONWebTokenAuthentication):
    def authenticate(self, request):
        jwt_value = str(request.META.get('HTTP_AUTHORIZATION'))
        #认证
        try:
            payload = jwt_decode_handler(jwt_value)
        except Exception:
            raise exceptions.AuthenticationFailed("认证失败")
        user = self.authenticate_credentials(payload)
        return user,None