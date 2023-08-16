from django.urls import path
from first_app.views import add_task

urlpatterns = [
    path('',add_task)
]
