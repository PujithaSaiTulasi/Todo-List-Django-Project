from django.db import models

# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title