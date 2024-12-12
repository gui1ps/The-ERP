from . import views
from django.urls import path

urlpatterns = [
    path('',views.get_stock, name='get_stock'),
    path('edit/',views.edit_stock, name='edit_stock')
]