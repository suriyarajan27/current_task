from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signn, name='signn.html'),
    path('loginn/', views.loginn, name='loginn.html'),
    path('todopath/',views.todopath, name='todopath.html'),
    path('DeleteTask/<str:name>/', views.DeleteTask, name='delete'),
    path('UpdateTask/<str:name>/', views.UpdateTask, name='update'),
]