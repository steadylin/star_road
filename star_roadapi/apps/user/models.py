from django.db import models
from django.contrib.auth.models import AbstractUser
from video.models import Video


class User(AbstractUser):
    mobilephone = models.CharField(max_length=11, unique=True)
    icon = models.ImageField(upload_to='icon', default='icon/default.png')
    signature = models.CharField(max_length=200, help_text='最大长度200', default='分享美好生活')
    sex = models.CharField(verbose_name='性别', default='女生', max_length=12)
    is_vip = models.BigIntegerField(verbose_name='会员', default=0)
    vip_expire = models.FloatField(verbose_name='会员过期时间', null=True)

    # 外键
    collect = models.ManyToManyField(Video)
