from . import views
from django.urls import path

urlpatterns=[
    path('',views.get_sales,name='get_sales'),
    path('create/',views.create_sales,name='create_sales')
]