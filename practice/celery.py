import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practice.settings')

app = Celery('practice')

# Using a string here means the worker doesn't
# have to serialize the configuration object to
# child processes. - namespace='CELERY' means all
# celery-related configuration keys should
# have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# Specify the worker_uid to run Celery tasks as a different user
# app.conf.worker_uid = 'celeryuser'

