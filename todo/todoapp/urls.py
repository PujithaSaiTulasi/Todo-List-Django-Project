from django.urls import path
from .views import get_todos, create_task, update_task, delete_task, mark_task_completed

urlpatterns = [
    path('', get_todos, name='get_todos'),
    path('create/', create_task, name='create_task'),
    path('update/<int:task_id>/', update_task, name='update_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('mark_completed/<int:task_id>/', mark_task_completed, name='mark_task_completed'),
]
