from django.shortcuts import render,redirect
from .forms import Note_form
from .models import Notes

def create(request):
    form=Note_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    

def update(request,pk):
    data={}
    data['db']=Notes.objects.get(pk=pk)
    form=Note_form(request.POST or None, instance=data['db'])
    if(form.is_valid()):
        form.save()
        return redirect('home')
