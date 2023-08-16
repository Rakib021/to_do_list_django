from django.contrib import admin

from first_app.models import TaskModel


# Register your models here.


class TaskStoreModelAdmin(admin.ModelAdmin):
    list_display =('id','taskTitle','taskDescription','is_completed')
    
admin.site.register(TaskModel,TaskStoreModelAdmin)