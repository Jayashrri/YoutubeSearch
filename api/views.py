from rest_framework.decorators import api_view
from rest_framework import generics

from .models import Video
from .utils import VideoSerializer, VideoPagination


class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all().order_by("-published_at")
    serializer_class = VideoSerializer
    pagination_class = VideoPagination
