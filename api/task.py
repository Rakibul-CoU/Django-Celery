


import time
import DjangoCelery
from api.models import Task, TaskResult

@DjangoCelery.celery_app.task()
def send_for_pool(task_id):
    send_for_list(task_id)
    return True



def send_for_list(task_id):
    for i in range(5):
        TaskResult.objects.create(task_id=task_id)
        time.sleep(60)

    return True