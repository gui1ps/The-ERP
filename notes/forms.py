from django.forms import ModelForm
from django import forms
from .models import Notes

class Note_form(ModelForm):
    class Meta:
        model=Notes
        fields=['title','content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control poppins-regular bg-transparent border-0', 'placeholder': 'Título'}),
            'content': forms.Textarea(attrs={'class': 'form-control poppins-regular  bg-transparent border-0', 'rows': 5,'placeholder': 'Escreva aqui'}),
        }
