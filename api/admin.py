from django.contrib import admin

from api.models import Task, TaskResult

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ("task_name",)

class TaskResultAdmin(admin.ModelAdmin):
    list_display = ("task_id",)

admin.site.register(Task, TaskAdmin)
admin.site.register(TaskResult, TaskResultAdmin)
