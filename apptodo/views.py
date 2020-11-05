from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import *
from django.views import View
class Index(View):
    def get(self,request):
        task=Task.objects.all()
        form=TaskForm()
        content={
            'tasks':task,
            'form':form,
        }
        return render(request,'index.html',content)


    def post(self,request):
        form=TaskForm()  #create form object
        form=TaskForm(request.POST)
        if form.is_valid():
            print("successful")
            print(form.cleaned_data['title'])
            title=form.cleaned_data['title']
            reg=Task(title=title)
            reg.save()
            return redirect('/')
        else:
            print("do again")  
       
        return render(request,'index.html',{'form':form})
    



def update(request,workid):
        #work_id=request.GET.get('workid')
        form=Task.objects.get(id=workid)
        if request.method=='POST':
            if form:
                c=request.POST['title']
                b=Task(title=c)
                b.update()
        return render(request,'update.html',{'form':form})


def delete_task(request,workid):
    delete_item=Task.objects.get(id=workid)
    delete_item.delete()
    return redirect('/')

    

    



