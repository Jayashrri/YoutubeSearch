from celery.task.schedules import crontab
from celery.decorators import periodic_task

from .helpers import getLatestVideos

@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="get_video_data",
    ignore_result=True
)
def get_video_data():
    getLatestVideos()