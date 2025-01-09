from django.forms import ModelForm
from django import forms
from .models import Products
from suppliers.models import Suppliers

class Product_Form(ModelForm):
    class Meta:
        model=Products
        fields=['name','reference','unit','local','p_cost','p_sell','profit',"supplier"]
        base_styles="form-control border-primary bg-transparent"
        base_styles_select="form-select border-primary bg-transparent"
        widgets = {
            'name': forms.TextInput(attrs={'class':base_styles,'id':'name','placeholder':'Nome'}),
            'reference': forms.TextInput(attrs={'class':base_styles,'id':'referencia','placeholder':'Referência'}),
            'local': forms.TextInput(attrs={'class':base_styles,'id':'local','placeholder':'Localização'}),
            'p_cost':forms.NumberInput(attrs={'class':base_styles,'id':'p_cost'}),
            'p_sell':forms.NumberInput(attrs={'class':base_styles,'id':'p_cost'}),
            'profit':forms.NumberInput(attrs={'class':base_styles,'id':'p_cost'}),
            'unit':forms.Select(attrs={'class':base_styles_select,'id':'unit'}),
            'supplier':forms.Select(attrs={'class':base_styles_select,'id':'supplier'})
        }