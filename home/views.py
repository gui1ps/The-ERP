from django.shortcuts import render
from notes.forms import Note_form
from notes.models import Notes

def home(request):
    data={}
    data['db']=Notes.objects.all()
    data['form']=[]
    for obj in data['db']:
        data['form'].append(Note_form(instance=obj)) 
    data['db_form'] = zip(data['form'], data['db'])
    return render(request,'home.html',data)