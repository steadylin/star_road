from rest_framework import serializers
from . import models
from rest_framework import serializers
from . import models


class BannerModelSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = models.Banner
        fields = ['name', 'link', 'img']
