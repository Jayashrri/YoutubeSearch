from rest_framework import serializers
from rest_framework import pagination

from .models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ["video_id", "title", "description", "published_at", "thumbnail"]


class VideoPagination(pagination.PageNumberPagination):
    page_size = 10
