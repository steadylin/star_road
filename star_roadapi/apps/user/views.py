from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from . import serializer
from star_roadapi.utils.response import APIResponse
from user import models
from rest_framework.exceptions import ValidationError


# 用户登录接口
class UserView(ViewSet):
    # 多方式登录
    authentication_classes = []  # 禁用jwt

    @action(methods=['POST'], detail=False)
    def login(self, request, *args, **kwargs):
        user_ser = serializer.UserModelSerializer(data=request.data)
        if user_ser.is_valid():  # 自定义了全局异常，不需要使用raise_exception=True
            # 从序列化对象user_ser.context中获取token和用户名
            token = user_ser.context['token']
            username = user_ser.context['user'].username
            id = user_ser.context['user'].id
            signature = user_ser.context['user'].signature
            sex = user_ser.context['user'].sex
            email = user_ser.context['user'].email
            avatar = str(user_ser.context['user'].icon)
            return APIResponse(token=token, username=username, id=id, signature=signature, sex=sex, email=email,
                               avatar=avatar)
        else:
            return APIResponse(code=0, msg=user_ser.errors)  # 序列化校检失败，返回错误信息

    # 判断手机号是否存在
    @action(detail=False)
    def check_telephone(self, request, *args, **kwargs):
        import re
        telephone = request.query_params.get('telephone')
        if not re.match('^[1][3-9][0-9]{9}$', telephone):
            return APIResponse(code=0, msg='手机号不合法')
        try:
            models.User.objects.get(mobilephone=telephone)
            return APIResponse(code=1)
        except:
            return APIResponse(code=0, msg='手机号不存在')

    # 验证码登录接口
    @action(methods=['POST'], detail=False)
    def code_login(self, request, *args, **kwargs):
        ser = serializer.CodeUserSSerializer(data=request.data)
        if ser.is_valid():
            token = ser.context.get('token')
            username = ser.context.get('user').username
            id = ser.context['user'].id
            signature = ser.context['user'].signature
            sex = ser.context['user'].sex
            email = ser.context['user'].email
            avatar = str(ser.context['user'].icon)
            return APIResponse(token=token, username=username, id=id, signature=signature, sex=sex, email=email,
                               avatar=avatar)
        else:
            return APIResponse(code=0, msg=ser.errors)

    # 修改用户资料
    # from utils.authentication import MyAuthentication
    # authentication_classes = [MyAuthentication, ]  # 禁用jwt

    @action(methods=['PUT'], detail=False)
    def change(self, request, *args, **kwargs):
        # print(request.data)
        pk = request.data.pop('pk')
        user_obj = models.User.objects.filter(pk=pk[0]).first()
        user_ser = serializer.ChangeSerializer(instance=user_obj, data=request.data)
        if user_ser.is_valid():
            user_ser.save()
            return APIResponse(data=user_ser.data)
        else:
            return APIResponse(status=101, msg='校检失败')


# 修改密码
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import UpdateModelMixin


class ChangePwdViewSet(GenericViewSet, UpdateModelMixin):
    queryset = models.User.objects.all()
    serializer_class = serializer.ChangePwdSerializers

    def update(self, request, *args, **kwargs):
        pk = request.data.get('pk')
        if pk:
            re_password = request.data.get('re_password')  # 不能使用pop
            new_password = request.data.get('new_password')
            if re_password == new_password:
                user = models.User.objects.filter(pk=pk).first()
                password = request.data.get('password')
                user_obj = user.check_password(password)
                if user_obj:
                    user.set_password(new_password)
                    user.save()
                    return APIResponse()
                else:
                    raise ValidationError('原密码错误')
            else:
                raise ValidationError('两次密码不一致')
        else:
            raise ValidationError('没有pk值')


# 发送短信接口
from star_roadapi.utils.throttings import SMSThrotting


class SendSmsView(ViewSet):
    throttle_classes = [SMSThrotting]

    # 发送短信接口
    authentication_classes = []  # 禁用jwt

    @action(methods=['GET'], detail=False)
    def send(self, request, *args, **kwargs):
        print('0')
        """
        发送验证码接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # 先判断是不是手机号
        import re
        from star_roadapi.libs.tx_sms import get_code, \
            send_str_code  # 因为tx_sms的init导入了get_code，send_str_code所以可以不用.send直接导到这两个方法
        from django.core.cache import cache  # 导入django缓存
        from django.conf import settings
        print(111)
        mobilephone = request.query_params.get('telephone')
        if not re.match('^1[3-9][0-9]{9}$', mobilephone):
            print('1')
            return APIResponse(code=0, msg='手机号不合法')  # code=0表示不合法，code=1是0k
        code = get_code()
        result = send_str_code(mobilephone, code)
        # 验证码存到django缓存中
        cache.set(settings.PHONE_CACHE_KEY % mobilephone, code, 180)  # 过期时间180秒，3分钟
        print('2')
        if result:
            return APIResponse(code=1, msg='验证码发送成功')
        else:
            return APIResponse(code=0, msg='验证码发送失败')


# 注册接口
from rest_framework.mixins import CreateModelMixin


class RegisterGenericViewSet(GenericViewSet, CreateModelMixin):
    queryset = models.User.objects.all()
    serializer_class = serializer.RegisterModelSerializer
    authentication_classes = []  # 禁用jwt

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        username = response.data.get('username')
        return APIResponse(code=1, msg='注册成功', username=username)


# 点赞、收藏接口
from video.models import Video


class UpCollectGenericViewSet(GenericViewSet, UpdateModelMixin):
    queryset = models.User.objects.all()
    serializer_class = serializer.UserModelSerializer

    def update(self, request, *args, **kwargs):
        # print(request.data)
        user_pk = request.data.get('user_pk')
        video_pk = request.data.get('video_pk')
        # print(user_pk,video_pk)
        if user_pk and video_pk:
            user = models.User.objects.filter(pk=user_pk).first()
            video = Video.objects.filter(pk=video_pk).first()
            # 加赞
            up = video.up
            up += 1
            Video.objects.filter(pk=video_pk).update(up=up)
            user.collect.add(video)
            return APIResponse(msg='点赞成功', up=up)
        else:
            # print(user_pk, video_pk)
            raise ValidationError('用户pk或视频pk错误')
