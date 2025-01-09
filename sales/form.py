from django import forms
from .models import Sale, Payment_Method, SaleProduct
from django.forms import modelformset_factory

base_styles_select="form-select border-primary bg-transparent"
base_styles="form-control border-primary bg-transparent"

class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model=Payment_Method
        fields=['name']

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['paymentmethod', 'customer', 'total']
        widgets={
            'customer':forms.Select(attrs={'class':base_styles_select, 'id':'customer'})
        }


class SaleProductForm(forms.ModelForm):
    class Meta:
        model = SaleProduct
        fields = ['product', 'quantity', 'price']
        widgets={
            'product':forms.Select(attrs={'class':base_styles_select,'id':'product'}),
            'quantity':forms.NumberInput(attrs={'class':base_styles,'id':'quantity'}),
            'price':forms.NumberInput(attrs={'class':base_styles,'id':'price','disabled':'disabled'})

        }


SaleFormFormSet=modelformset_factory(
    SaleProduct,
    form=SaleProductForm,
    fields=['product', 'quantity', 'price'],
    extra=1
)