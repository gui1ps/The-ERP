from . import views
from django.urls import path

urlpatterns = [
    path('',views.get_suppliers,name='get_suppliers'),
    path('form/',views.form, name='form_suppliers'),
    path('create/',views.create_supplier, name='create_supplier'),
    path('edit/<int:pk>/',views.edit_supplier, name='edit_supplier'),
    path('update/<int:pk>/',views.update_supplier, name='update_supplier'),
    path('delete/<int:pk>/',views.delete_supplier, name='delete_supplier'),
]