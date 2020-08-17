from rest_framework import serializers
from . import models


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Film
        fields = ['id',
                  'name',
                  'describe',
                  'heat',
                  'is_vip',
                  'film_url',
                  'img_url']
        extra_kwargs = {
            'id': {'read_only': True},
        }
