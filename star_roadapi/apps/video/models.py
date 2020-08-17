from django.db import models

# Create your models here.
from utils.models import BaseModel


class Video(BaseModel):
    name = models.CharField(max_length=32, verbose_name='视频名称', default='star_road视频社区')
    img = models.ImageField(upload_to="courses", max_length=255, verbose_name="封面图片", blank=True, null=True)
    vide_url = models.CharField(max_length=1000, verbose_name='视频链接')
    author = models.CharField(max_length=32, verbose_name='视频作者', default='joab')
    up = models.BigIntegerField(verbose_name='点赞数', default=186)




