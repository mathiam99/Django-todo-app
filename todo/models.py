from django.db import models
import datetime

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    posted_date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)
    programmed_date = models.DateField(auto_now=False, auto_now_add=False, default=datetime.datetime.now())

    def __str__(self):
        return self.title