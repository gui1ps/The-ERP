from django import forms
from django.forms import modelformset_factory
from .models import Stock

class StockForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields=['quantity']

StockFormSet=modelformset_factory(
    Stock,
    form=StockForm,
    fields=['quantity'],
    extra=0
)