from django.contrib import admin
from django.urls import path, include
from .views import TaskList, TaskInfo, CreateTask, DeleteTask, UpdateTask, UpdateTaskStatus

urlpatterns = [
    # TODO LIST without auth
    path('task-list/', TaskList),
    path('task-detail/<str:pk>/', TaskInfo),
    path('task-create/', CreateTask),
    path('task-update-status/<str:pk>/', UpdateTaskStatus),
    path('task-update/<str:pk>/', UpdateTask),
    path('task-delete/<str:pk>/', DeleteTask),
]