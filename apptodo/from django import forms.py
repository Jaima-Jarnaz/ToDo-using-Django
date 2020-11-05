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
    <div class="col-6">
                <a href="{% url 'update' task.id %}" class="btn btn-warning btn-sm mt-2" name=""  data-toggle="modal" data-target="#exampleModal1">Update</a>
                <a href="/?workid={{task.id}}" class="btn btn-danger btn-sm mt-2">Delete</a>
            </div> 

            ef update(request,workid):
        #work_id=request.GET.get('workid')
        task=Task.objects.get(id=workid)
        form=TaskForm(instance=task)
        if request.method=='POST':
            form=TaskForm(request.POST,instance=task)
            if form.is_valid():
                form.save()
                return redirect('/')
        return render(request,'update.html',{'form':form})
    