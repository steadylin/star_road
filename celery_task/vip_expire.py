# 一、加载django配置环境
import os, sys
import django

# 获取到项目的根目录
PROJECT_ROOT = os.path.dirname(os.path.abspath('__file__'))
# 把项目的根目录放到 sys.path 中
sys.path.insert(0, PROJECT_ROOT)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'star_roadapi.settings.dev')
django.setup()
from .celery import app

from user.models import User
from star_roadapi.utils.logger import log
import time


@app.task
def expire():
    obj_list = User.objects.filter(is_vip=1)
    for obj in obj_list:
        if obj.vip_expire <= time.time():
            user_id = obj.id
            User.objects.filter(id=obj.id).update(is_vip=0)
            log.info(f'用户ID{user_id}会员已过期')
            return f'用户ID{user_id}会员已过期'
        else:
            return '没有过期会员'
    return '没有会员用户'
