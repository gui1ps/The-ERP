from . import views
from django.urls import path

urlpatterns = [
    path('',views.get_customers,name='get_customers'),
    path('form/',views.form, name='form_customer'),
    path('create/',views.create_customer, name='create_customer'),
    path('edit/<int:pk>/',views.edit_customer, name='edit_customer'),
    path('update/<int:pk>/',views.update_customer, name='update_customer'),
    path('delete/<int:pk>/',views.delete_customer, name='delete_customer'),
]