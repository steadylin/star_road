from django.db import models

# Create your models here.

from utils.models import BaseModel


class Film(BaseModel):
    name = models.CharField(max_length=50, verbose_name='名字')
    describe = models.CharField(max_length=20, verbose_name='描述')
    heat = models.BigIntegerField(verbose_name='热度')
    is_vip = models.BigIntegerField(verbose_name='收费', default=0)
    film_url = models.CharField(max_length=1000, verbose_name='电影地址')
    img_url = models.CharField(max_length=200, verbose_name='封面地址')


