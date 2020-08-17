from rest_framework import serializers
from . import models


class ImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Img
        fields = ('pk', 'title', 'img_url')
