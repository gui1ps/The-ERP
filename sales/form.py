from django import forms
from .models import Sale, Payment_Method, SaleProduct
from django.forms import modelformset_factory

class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model=Payment_Method
        fields=['name']

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['paymentmethod', 'customer', 'total']

class SaleProductForm(forms.ModelForm):
    class Meta:
        model = SaleProduct
        fields = ['product', 'quantity', 'price']


SaleFormFormSet=modelformset_factory(
    SaleProduct,
    form=SaleProductForm,
    fields=['product', 'quantity', 'price'],
    extra=0
)