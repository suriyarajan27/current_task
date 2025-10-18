from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signn, name='signn.html'),
    path('loginn/', views.loginn, name='loginn.html'),
    path('todopage/', views.todopage, name='todopage')
]