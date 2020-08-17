from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework import mixins
from . import models, serializers

from django.conf import settings


class BannerView(GenericViewSet, ListModelMixin):
    # 无论有多少条待展示的数据，最多就展示3条
    authentication_classes = []  # 禁用jwt
    queryset = models.Banner.objects.filter(is_delete=False, is_show=True).order_by('display_order')[
               :settings.BANNER_COUNTER]
    serializer_class = serializers.BannerModelSerilaizer


















