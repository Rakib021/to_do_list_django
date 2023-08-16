from django.urls import path
from first_app.views import add_task,show_task,edit_task,delete_task,com_task,delete_task_com

urlpatterns = [
    path('',add_task,name="addTask"),
    path('show_task/',show_task,name="showtask"),
    path('edit_task/<int:id>',edit_task,name="edit_task"),
    path('delete_task/<int:id>',delete_task,name="delete_task"),
    path('com_task/<int:id>', com_task, name = 'com_task'),
    path('delete_task_com/<int:id>', delete_task_com, name = 'delete_task_com'),
]
