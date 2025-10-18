from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todolist import models
from todolist.models import TODOO

def signn(request):
    if request.method == "POST":

        fnm = request.POST.get('fnm')

        emailid = request.POST.get('emailid')

        pwd = request.POST.get('pwd')

        print(fnm, emailid, pwd)

        my_user = User.objects.create_user(

            fnm, emailid, pwd

        )
        my_user.save()

        return redirect(request, 'todopage/')
    
    return render(request, 'signn.html')

def loginn(request):

    return render(request, 'loginn.html')

def todopage(request):
    
    return render(request, 'todo.html')