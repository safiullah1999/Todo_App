from django.contrib import admin
from django.urls import path, include
from .views import TaskList, TaskInfo, CreateTask, DeleteTask, UpdateTask, UpdateTaskStatus, UserDetailView, TodoListView, Logout
from .auth import CustomAuthToken

urlpatterns = [
    # TODO LIST with auth
    path('register', UserDetailView.as_view()),
    path('login', CustomAuthToken.as_view()),
    path('add', TodoListView.as_view()),
    path('getTodoList/<int:id>', TodoListView.as_view()),
    path('logout', Logout.as_view()),

    # TODO LIST without auth
    path('task-list/', TaskList),
    path('task-detail/<str:pk>/', TaskInfo),
    path('task-create/', CreateTask),
    path('task-update-status/<str:pk>/', UpdateTaskStatus),
    path('task-update/<str:pk>/', UpdateTask),
    path('task-delete/<str:pk>/', DeleteTask),
]