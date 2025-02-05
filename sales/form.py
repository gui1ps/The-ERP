from django import forms
from .models import Sale, Payment_Method, SaleProduct
from django.forms import modelformset_factory

base_styles_select="form-select border-primary bg-transparent"

class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model=Payment_Method
        fields=['name']

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['paymentmethod', 'customer', 'total']
        widgets={
            'customer':forms.Select(attrs={'class':base_styles_select, 'id':'customer'}),
            'paymentmethod':forms.Select(attrs={'class':base_styles_select, 'id':'paymentmethod'}),
            'total':forms.NumberInput(attrs={'class':'border-0 w-100','readonly':'readonly'}),
        }

class SaleProductForm(forms.ModelForm):
    class Meta:
        model = SaleProduct
        fields = ['product', 'quantity', 'price']

SaleFormFormSet=modelformset_factory(
    SaleProduct,
    form=SaleProductForm,
    fields=['product', 'quantity', 'price'],
    extra=0,
)