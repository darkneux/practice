from .tasks import is_CeleryWorking
from django.shortcuts import redirect,render
def check_celery(request):
    print("HELLO VIVEK")
    is_CeleryWorking.delay()
    return redirect("/")
