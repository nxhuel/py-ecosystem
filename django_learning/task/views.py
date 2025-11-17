from rest_framework.generics import ListCreateAPIView
from task.models import TaskModel
from task.serializer import TaskSerializer

# Create your views here.

class TaskListCreateView(ListCreateAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer