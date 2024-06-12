from django.http import HttpResponse
from django.shortcuts import render

from api.models import Task
from api.task import send_for_pool

# Create your views here.


def auto_reject(request):
    task = Task.objects.all()
    for i in task:
        send_for_pool.delay(i.pk)

    return HttpResponse("Task sent for pool")