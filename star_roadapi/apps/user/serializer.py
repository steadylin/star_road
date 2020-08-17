from rest_framework import serializers
from user import models
import re
from rest_framework.exceptions import ValidationError

from rest_framework_jwt.utils import jwt_encode_handler, jwt_payload_handler

from rest_framework import serializers
from . import models
from rest_framework.exceptions import ValidationError


class UserModelSerializer(serializers.ModelSerializer):
    username = serializers.CharField()  # username为unique字段，需要重定义

    class Meta:
        model = models.User
        fields = ('username', 'password', 'id', 'signature', 'sex', 'email')
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True},
            'signature': {'read_only': True},
            'sex': {'read_only': True},
            'email': {'read_only': True},
        }

    # 全局钩子，判断多方式登录
    def validate(self, attrs):
        # _get_user去获取用户对象
        user = self._get_user(attrs)
        # 去获取签发的token
        token = self._get_token(user)
        self.context['token'] = token
        self.context['user'] = user
        return attrs

    # 获取用户名
    def _get_user(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        import re
        # 判断用户名类型
        if re.match('^1[3-9][0-9]{9}$', username):  # 匹配usernmae是不是手机号类型
            user = models.User.objects.filter(mobilephone=username).first()
        elif re.match('^.*@.*$', username):
            user = models.User.objects.filter(email=username).first()
        else:
            user = models.User.objects.filter(username=username).first()
        if user:
            ret = user.check_password(password)
            if ret:
                return user
            else:
                raise ValidationError('密码错误')
        else:
            raise ValidationError('用户不存在')

    # 获取token
    def _get_token(self, user):
        from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
        payload = jwt_payload_handler(user)  # 加入user得到payload
        token = jwt_encode_handler(payload)  # 加入patload得到token
        return token


# 验证码序列化器
class CodeUserSSerializer(serializers.ModelSerializer):
    code = serializers.CharField()
    telephone = serializers.CharField(source='mobilephone')

    class Meta:
        model = models.User
        fields = ('telephone', 'code', 'id', 'signature', 'sex', 'email')
        extra_kwargs = {
            'id': {'read_only': True},
            'signature': {'read_only': True},
            'sex': {'read_only': True},
            'email': {'read_only': True},
        }

    # 全局钩子,验证码登录成功签发token
    def validate(self, attrs):
        # _get_user去获取用户对象
        user = self._get_user(attrs)
        # 去获取签发的token
        token = self._get_token(user)
        self.context['token'] = token
        self.context['user'] = user
        return attrs

    # 获取用户名
    def _get_user(self, attrs):
        from django.core.cache import cache
        from django.conf import settings
        import re
        mobilephone = attrs.get('mobilephone')
        code = attrs.get('code')
        # 取出原来的code
        cache_code = cache.get(settings.PHONE_CACHE_KEY % mobilephone)
        if code == '0000' or code == cache_code:  # 万能验证码#if code == cache_code:
            # 验证码用过一次就更新为空
            cache.set(settings.PHONE_CACHE_KEY % mobilephone, '')
            user = models.User.objects.filter(mobilephone=mobilephone).first()
            # 验证成功返回用户
            return user
        else:
            raise ValidationError('验证码错误，请重新输入')

    # 获取token
    def _get_token(self, user):
        from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
        payload = jwt_payload_handler(user)  # 加入user得到payload
        token = jwt_encode_handler(payload)  # 加入patload得到token
        return token


# 注册序列化器
from django.core.cache import cache
from django.conf import settings


class RegisterModelSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=4, min_length=4, write_only=True)
    telephone = serializers.CharField(source='mobilephone')

    class Meta:
        model = models.User
        fields = ('username', 'telephone', 'code', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'read_only': True},
        }

    def validate(self, attrs):
        print(attrs)
        telephone = attrs.get('mobilephone')
        code = attrs.get('code')
        cache_code = cache.get(settings.PHONE_CACHE_KEY % telephone)
        if code == cache_code or code == '0000':
            import re
            if re.match('^[1][3-9][0-9]{9}$', telephone):
                attrs['username'] = telephone
                attrs.pop('code')
                return attrs
            else:
                raise ValidationError('手机不合法')
        else:
            raise ValidationError('验证码有误')

    # 重新create方法
    def create(self, validated_data):
        user = models.User.objects.create_user(**validated_data)
        return user


# 修改密码
class ChangePwdSerializers(serializers.ModelSerializer):
    newpassword = serializers.CharField()

    class Meta:
        model = models.User
        fields = ['password', 'newpassword']
        extra_kwargs = {
            'password': {'write_only': True},
            'newpassword': {'write_only': True},
        }

        # def update(self, instance, validated_data):
        #     print('update')
        #     password = validated_data.get('password')
        #     new_password = validated_data.get('new_password')
        #     user = models.User.check_password(instance, password)
        #     user.set_password(password=new_password)





# 修改用户资料序列化器
class ChangeSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = models.User
        fields = ['username', 'signature', 'icon', 'sex', 'email']
        extra_kwargs = {
        }









