
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings
# 替换admin
import xadmin

xadmin.autodiscover()
# xversion模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion

xversion.register_models()
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    # 开放media文件夹
    re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
    # 路由分发
    path('home/', include('home.urls')),
    path('user/', include('user.urls')),
    path('video/', include('video.urls')),
    path('img/', include('img.urls')),
    path('order/', include('order.urls')),
    path('film/', include('film.urls')),
]
