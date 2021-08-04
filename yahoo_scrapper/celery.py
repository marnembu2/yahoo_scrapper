from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yahoo_scrapper.settings')
app = Celery('yahoo_scrapper')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(['yahoo_scrapper'])


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')





