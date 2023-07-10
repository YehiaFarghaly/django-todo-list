from django.db import models

# Create your models here.
class TodoTask(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text