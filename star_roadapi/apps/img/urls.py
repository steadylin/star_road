from django.urls import path, include
from . import views


urlpatterns = [
    # path('', views.ImgGenericAPIView.as_view()),
    path('page/', views.ImgView.as_view()),
    path('post/', views.PostCreateAPIView.as_view()),
]







