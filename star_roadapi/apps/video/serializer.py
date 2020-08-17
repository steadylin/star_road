from rest_framework import serializers
from . import models


class videoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Video
        exclude = ('img',)



