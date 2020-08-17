from django.db import models

# Create your models here.
from utils.models import BaseModel


class Img(BaseModel):
    title = models.CharField(max_length=32, verbose_name='图片标题', default='妹子图')
    # img_site = models.ImageField(upload_to='img', verbose_name='妹子图', null=True)
    img_url = models.ImageField(upload_to='img', verbose_name='妹子图', unique=True)




