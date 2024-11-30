from django.forms import ModelForm
from django import forms
from .models import Products

class Product_Form(ModelForm):
    class Meta:
        model=Products
        fields=['name','reference','unit','local','p_cost','p_sell','profit']
        base_styles="form-control border-primary bg-transparent"
        widgets = {
            'name': forms.TextInput(attrs={'class':base_styles,'id':'name','placeholder':'Nome'}),
            'reference': forms.TextInput(attrs={'class':base_styles,'id':'referencia','placeholder':'Referência'}),
            'local': forms.TextInput(attrs={'class':base_styles,'id':'local','placeholder':'Localização'}),
            'p_cost':forms.NumberInput(attrs={'class':base_styles,'id':'p_cost'})
        }