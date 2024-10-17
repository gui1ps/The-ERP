from . import views
from django.urls import path

urlpatterns = [
    path('create/',views.create, name='create_note'),
    path('update/<int:pk>/',views.update, name='update_note')
]