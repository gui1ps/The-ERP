from django.shortcuts import render,HttpResponse,redirect
from .models import Sale
from .form import *
from stock.models import Stock

def get_sales(request):
    sales=Sale.objects.all()
    data={}
    data['data']=sales
    return render(request,'sales.html',data)

def create_sales(request):
    if request.method == 'POST':
        sale_form = SaleForm(request.POST)
        sale_product_formset = SaleFormFormSet(request.POST)
        if sale_form.is_valid() and sale_product_formset.is_valid():
            sale = sale_form.save()
            sale_products = sale_product_formset.save(commit=False)
            for sale_product in sale_products:
                sale_product.sale = sale
                sale_product.save()
            return redirect('get_sales')
        else:
            print(sale_form.errors)
            print(sale_product_formset.errors)
            return HttpResponse(f'Formulários inválidos: {sale_form.errors}, {sale_product_formset.errors}')

    else:
        data={}
        data['form']=SaleForm()
        data['formset']=SaleFormFormSet(queryset=SaleProduct.objects.none())
        return render(request, 'sales_form.html',data)
