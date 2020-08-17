from django.shortcuts import render

# Create your views here.
from . import models
from . import serializer
from utils.userpermission import UserPermission
# 分页器
from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = "page"


from rest_framework.generics import ListAPIView


# ListAPIView等视图类的使用分页器的方法
class ImgView(ListAPIView):
    queryset = models.Img.objects.all()
    serializer_class = serializer.ImgSerializer
    # 配置分页
    pagination_class = MyPageNumberPagination
    authentication_classes = []  # 禁用jwt
    # permission_classes = [UserPermission, ]




#接受定时接口
from rest_framework.generics import CreateAPIView
class PostCreateAPIView(CreateAPIView):
    queryset = models.Img.objects.all()
    serializer_class = serializer.ImgSerializer
    authentication_classes = []  # 禁用jwt





