from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from task.models import TaskModel
from task.serializer import TaskSerializer

# Create your views here.

# Listar y crear tareas 
# GET api/v1/tasks
# POST api/v1/tasks 
class TaskListCreateView(ListCreateAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
    
# Obtener, actualizar y borrar tarea
# GET api/v1/tasks/1 → trae la task
# PUT api/v1/tasks/1 → actualiza todos los campos
# PATCH api/v1/tasks/1 → actualiza solo algunos
# DELETE api/v1/tasks/1 → elimina
class TaskDetailView(RetrieveUpdateDestroyAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
    
