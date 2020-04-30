import os
import apiclient

from django.utils.dateparse import parse_datetime
from datetime import datetime, timedelta

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

from .models import Video


def queryAPI(page_token, published_after):
    api_service_name = "youtube"
    api_version = "v3"
    developer_keys = []
    for developer_key in developer_keys:
        try:
            youtube_object = apiclient.discovery.build(
                api_service_name, api_version, developerKey=developer_key
            )

            request = youtube_object.search().list(
                pageToken=page_token,
                part="snippet",
                eventType="completed",
                maxResults=50,
                order="date",
                q="official",
                relevanceLanguage="en",
                type="video",
                publishedAfter=published_after,
            )
            response = request.execute()
        except apiclient.errors.HttpError:
            continue
        else:
            return response
    else:
        return None


def getLatestVideos():
    published_after = (datetime.utcnow() - timedelta(hours=12)).isoformat("T") + "Z"
    response = queryAPI("", published_after)
    if response:
        result = response["items"]
        page_token = response.get("nextPageToken", None)

        while page_token and (len(response["items"]) != 0):
            response = queryAPI(page_token, published_after)
            result.extend(response["items"])
            page_token = response.get("nextPageToken", None)

        new_videos = []

        for i, video in enumerate(result, 1):
            details = Video(
                id=i,
                video_id=video["id"]["videoId"],
                title=video["snippet"]["title"],
                description=video["snippet"]["description"],
                published_at=parse_datetime(video["snippet"]["publishedAt"]),
                thumbnail=video["snippet"]["thumbnails"]["default"]["url"],
            )

            new_videos.append(details)

        current_videos = Video.objects.order_by("-published_at")
        if (not current_videos) or (
            current_videos and current_videos[0].video_id != new_videos[0].video_id
        ):
            Video.objects.all().delete()
            Video.objects.bulk_create(new_videos)
