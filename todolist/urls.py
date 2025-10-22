from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signn, name='signn.html'),
    path('loginn/', views.loginn, name='loginn.html'),
    path('todopath/',views.todopath, name='todopath.html'),
    path('DeleteTask/<str:name>/', views.DeleteTask, name='Delete'),
    path('logout/', views.LogoutView, name='logout'),
    path('UpdateTask/<str:name>/', views.UpdateTask, name='Update'),
]