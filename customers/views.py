from django.shortcuts import render,redirect,HttpResponse
from .models import Customers
from .form import Customer_Form

def get_customers(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        data = {
            'data': Customers.objects.all()
        }
        return render(request, 'customers.html', data)

def form(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        data={}
        data['form']=Customer_Form()
        return render(request,'one_customer_form.html',data)

def create_customer(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        form=Customer_Form(request.POST or None)
        if(form.is_valid()):
            form.save()
            return redirect('get_customers')

def edit_customer(request,pk):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        data = {
            'data': Customers.objects.get(pk=pk),
        }
        data['form']=Customer_Form(instance=data['data'])
        return render(request,'one_customer_form.html',data)

def update_customer(request, pk):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        customer = Customers.objects.get(pk=pk)
        form = Customer_Form(request.POST or None, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('get_customers')
        else:
            return HttpResponse(form.errors)

def delete_customer(request,pk):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        customer=Customers.objects.get(pk=pk)
        customer.delete()
        return redirect('get_customers')