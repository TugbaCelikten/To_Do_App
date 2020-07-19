from django.db import models
from datetime import datetime

# Create your models here.

class Todos(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True)
    finised = models.BooleanField(default=False)
    datetime = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.title
    