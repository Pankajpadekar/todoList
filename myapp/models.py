from django.db import models

# Create your models here.

class Task(models.Model):
    task_Title = models.CharField(max_length=50)
    task_Desc = models.TextField()
    task_status = models.BooleanField(default=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_Title


