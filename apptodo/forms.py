from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(label='Your work', max_length=200)    
    #name = forms.CharField(label='your work', max_length=200)   