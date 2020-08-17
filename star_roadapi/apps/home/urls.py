from django.urls import path, re_path, include
from . import views

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('banner', views.BannerView)
urlpatterns = [
    # path('banner/', views.BannerView.as_view()),
    path('', include(router.urls)),
]
