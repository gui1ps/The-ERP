from django.shortcuts import render,redirect,HttpResponse
from products.models import Products
from products.form import Product_Form

def get_products(request):
    data={
        'data':Products.objects.all()
    }

    return render(request,'products.html',data)

def form(request):
    data={}
    data['form']=Product_Form()
    return render(request,'one_product_form.html',data)

def create_products(request):
    form=Product_Form(request.POST or None)
    if(form.is_valid()):
        form.save()
        return redirect('get_products')

def edit_products(request,pk):
    data = {
        'data': Products.objects.get(pk=pk),
    }
    data['form']=Product_Form(instance=data['data'])
    return render(request,'one_product_form.html',data)

def update_products(request, pk):
    customer = Products.objects.get(pk=pk)
    form = Product_Form(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('get_products')
    else:
        return HttpResponse(form.errors)

def delete_products(request,pk):
    customer=Products.objects.get(pk=pk)
    customer.delete()
    return redirect('get_products')