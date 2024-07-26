from django.db import models

# Create your models here.
"""
todo
    -name (string)
    -description (string)
    -status (boolean)
"""




class Task(models.Model):
    name = models.CharField(max_length=100)
    description=models.TextField()
    status=models.BooleanField(default=False)