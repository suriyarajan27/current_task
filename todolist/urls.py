from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('', views.signn, name='signn.html'),
    path('loginn/', views.loginn, name='loginn.html'),
    path('todopath/',views.todopath, name='todopath.html'),
    path('DeleteTask/<int:id>/', views.DeleteTask, name='Delete'),
    path('UpdateTask/<int:id>/', views.UpdateTask, name='Update'),
    path('logout/', views.LogoutView, name='logout'),

]