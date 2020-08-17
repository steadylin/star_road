from django.shortcuts import render

# Create your views here.
from . import models
from . import serializer

# 分页
from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = "page"


from rest_framework.generics import ListAPIView


# ListAPIView等视图类的使用分页器的方法
class FilmView(ListAPIView):
    queryset = models.Film.objects.all()
    serializer_class = serializer.FilmSerializer
    # 配置分页
    pagination_class = MyPageNumberPagination
    authentication_classes = []
