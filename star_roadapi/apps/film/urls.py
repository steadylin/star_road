from django.urls import path, re_path, include
from . import views
# 自动生成路由
# from rest_framework.routers import SimpleRouter
#
# router = SimpleRouter()
# router.register('', views.FilmModelViewSet, 'film')

urlpatterns = [
    # path('', include(router.urls)),
    path('page/', views.FilmView.as_view()),
]
# urlpatterns += router.urls
