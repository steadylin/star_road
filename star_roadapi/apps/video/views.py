from django.shortcuts import render

# Create your views here.


from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from . import models
from . import serializer


class VideoGenericView(GenericAPIView):
    queryset = models.Video.objects.all()
    serializer_class = serializer.videoSerializer
    def get(self, request, *args, **kwargs):
        import random
        # pk = random.choice([i for i in range(1, 117)])
        video_obj = random.choice(self.get_queryset())
        video_ser = self.get_serializer(video_obj)
        # print(video_obj)
        return Response(video_ser.data)







