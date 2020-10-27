from django import forms
from django.forms import ModelForm
from .models import *
class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields='__all__'




        from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import TaskForm
def index(request):
    task=Task.objects.all()
    form=TaskForm()
    if request.method =='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            print("successful")
        return redirect('/')
    else:
        print("sry")


    content={
        'tasks':task,
        'form':form
    }
    return render(request,'index.html',content)


from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(label='your work', max_length=200)    