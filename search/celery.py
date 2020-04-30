import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'search.settings')

app = Celery('search')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()