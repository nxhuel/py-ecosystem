from django.urls import path
from task.views import TaskListCreateView

urlpatterns = [
    path('v1/tasks', TaskListCreateView.as_view()),
    # path('v1/tasks/<int:id>',  TaskApiViewDetail.as_view())
]
