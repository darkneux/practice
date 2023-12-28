from celery import shared_task
import time
@shared_task
def is_CeleryWorking():
    time.sleep(5)
    print("Celery is Working Fine")