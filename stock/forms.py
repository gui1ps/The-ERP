from django import forms
from django.forms import modelformset_factory
from .models import Stock

base_styles_select="form-select border-primary bg-transparent"

class StockForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields=['quantity']
        widgets={'quantity':forms.NumberInput(attrs={'class':base_styles_select})}

StockFormSet=modelformset_factory(
    Stock,
    form=StockForm,
    fields=['quantity'],
    extra=0
)