import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sarma_box_tales.settings')

app = Celery('sarma_box_tales')


app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()