from django.urls import path
from task.views import TaskListCreateView, TaskDetailView

urlpatterns = [
    path('v1/tasks', TaskListCreateView.as_view()),
    path('v1/tasks/<int:pk>', TaskDetailView.as_view())
]
