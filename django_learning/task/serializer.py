from rest_framework.serializers import ModelSerializer
from task.models import TaskModel

class TaskSerializer(ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'