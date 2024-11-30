from . import views
from django.urls import path

urlpatterns = [
    path('',views.get_products,name='get_products'),
    path('form/',views.form, name='form_products'),
    path('create/',views.create_products, name='create_products'),
    path('edit/<int:pk>/',views.edit_products, name='edit_products'),
    path('update/<int:pk>/',views.update_products, name='update_products'),
    path('delete/<int:pk>/',views.delete_products, name='delete_products'),
]