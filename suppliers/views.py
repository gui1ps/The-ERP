from django.shortcuts import render,redirect,HttpResponse
from .models import Suppliers
from .form import Supplier_Form

def get_suppliers(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        data = {
            'data': Suppliers.objects.all()
        }
        return render(request, 'suppliers.html', data)

def form(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        data={}
        data['form']=Supplier_Form()
        return render(request,'one_supplier_form.html',data)

def create_supplier(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        form=Supplier_Form(request.POST or None)
        if(form.is_valid()):
            form.save()
            return redirect('get_suppliers')

def edit_supplier(request,pk):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        data = {
            'data': Suppliers.objects.get(pk=pk),
        }
        data['form']=Supplier_Form(instance=data['data'])
        return render(request,'one_supplier_form.html',data)

def update_supplier(request, pk):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        supplier = Suppliers.objects.get(pk=pk)
        form = Supplier_Form(request.POST or None, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('get_suppliers')
        else:
            return HttpResponse(form.errors)

def delete_supplier(request,pk):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        supplier=Suppliers.objects.get(pk=pk)
        supplier.delete()
        return redirect('get_suppliers')