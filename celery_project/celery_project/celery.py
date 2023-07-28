from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_project.settings')

app = Celery('celery_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get-joke-3-seconds': {
        'task': 'jokes.tasks.get_joke',
        'schedule': 5.0,
    },
}

app.autodiscover_tasks()