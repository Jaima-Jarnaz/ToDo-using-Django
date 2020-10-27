from django.db import models
import datetime
class Task(models.Model):
    title    =models.CharField(max_length=300)
    complete =models.BooleanField(default=False)
    created  =models.DateTimeField(default=datetime.datetime.today)
 

def __str__(self):
    return self.title