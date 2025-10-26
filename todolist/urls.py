from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signn, name='signn'),
    path('loginn/', views.loginn, name='loginn'),
    path('todopath/',views.todopath, name='todopath'),
    path('DeleteTask/<str:name>/', views.DeleteTask, name='Delete'),
    path('logout/', views.LogoutView, name='logout'),
    path('UpdateTask/<str:name>/', views.UpdateTask, name='Update'),
]