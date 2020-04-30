from django.db import models

class Video(models.Model):
    video_id = models.CharField(max_length=20)
    title = models.TextField()
    description = models.TextField()
    published_at = models.DateTimeField()
    thumbnail = models.CharField(max_length=100)
