from django.urls import path, include, re_path
from . import views
# 自动生成路由
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', views.UserView, 'login')
router.register('', views.UserView, 'change')
router.register('', views.SendSmsView, 'send')  # 不要用as_view()，需要加上反向解析，不然不会报错
router.register('', views.ChangePwdViewSet, 'changepwd')
router.register('upcollect', views.UpCollectGenericViewSet, 'upcollect')
router.register('register', views.RegisterGenericViewSet, 'register')  # 用户注册接口

urlpatterns = [
]

urlpatterns += router.urls












