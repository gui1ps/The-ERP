from django.forms import ModelForm
from django import forms
from .models import Customers

class Customer_Form(ModelForm):
    class Meta:
        model=Customers
        fields=['name','b_date','type','document','street','number','neighborhood','city','state','postal_code','observations','email','phone']
        base_styles="form-control border-primary bg-transparent"
        base_styles_select="form-select border-primary bg-transparent"
        widgets = {
            'name': forms.TextInput(attrs={'class':base_styles,'id':'name','placeholder':'Nome'}),
            'b_date': forms.TextInput(attrs={'class':base_styles,'id':'b_date','placeholder':'Nascimento'}),
            'type': forms.Select(attrs={'class':base_styles_select,'id':'type','placeholder':'Tipo'}),
            'document': forms.TextInput(attrs={'class':base_styles,'id':'document','placeholder':'Documento'}),
            'street': forms.TextInput(attrs={'class':base_styles,'id':'street','placeholder':'Rua'}),
            'number': forms.TextInput(attrs={'class':base_styles,'id':'number','placeholder':'Número'}),
            'neighborhood': forms.TextInput(attrs={'class':base_styles,'id':'neighborhood','placeholder':'Bairro'}),
            'city': forms.TextInput(attrs={'class':base_styles,'id':'city','placeholder':'Cidade'}),
            'state': forms.TextInput(attrs={'class':base_styles,'id':'state','placeholder':'Estados'}),
            'postal_code': forms.TextInput(attrs={'class':base_styles,'id':'postal_code','placeholder':'CEP'}),
            'observations': forms.Textarea(attrs={'class':base_styles,'id':'observations','placeholder':'Observações'}),
            'email':forms.EmailInput(attrs={'class':base_styles,'id':'email','placeholder':'E-mail'}),
            'phone':forms.TextInput(attrs={'class':base_styles,'id':'phone','placeholder':'Telefone'}),
        }