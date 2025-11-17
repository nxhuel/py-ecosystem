from django.db import models

# Create your models here.

class TaskModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    completed = models.BooleanField()
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title} {self.description} {self.completed} {self.completed} {self.author} {self.created_at}'