from django.contrib import admin
from .models import Task

#show database
class AdminTask(admin.ModelAdmin):
    list_display=['title','complete','created']

admin.site.register(Task,AdminTask) #register model

