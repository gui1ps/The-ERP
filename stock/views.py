from django.shortcuts import render,redirect,HttpResponse
from .models import Stock
from django.contrib.auth.decorators import login_required
from .forms import StockFormSet

@login_required
def get_stock(request):
    data={
        'data':Stock.objects.select_related('product')
    }
    return render(request,'stocks.html',data)

@login_required
def edit_stock(request):
    queryset = Stock.objects.all()

    if request.method == 'POST':
        formset = StockFormSet(request.POST, queryset=queryset)
        if formset.is_valid():
            for form in formset:
                if form.has_changed():
                    form.save() 
            return redirect('get_stock')
    else:
        formset = StockFormSet(queryset=queryset)

    return render(request, 'stock_form.html', {'formset': formset})
