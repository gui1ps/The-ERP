from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('home.urls')),
    path('notes/', include('notes.urls')),
    path('customers/',include('customers.urls')),
    path('products/',include('products.urls')),
    path('suppliers/',include('suppliers.urls')),
    path('stock/',include('stock.urls')),
    path('sales/',include('sales.urls'))
]
