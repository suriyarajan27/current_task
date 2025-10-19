from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todolist import models
from todolist.models import TODOTASK
from django.contrib.auth import authenticate, login
from django.contrib import messages


def signn(request):
    if request.method=="POST":
        fnm=request.POST.get('fnm')
        emailid=request.POST.get('emailid')
        pwd=request.POST.get('pwd')
        print(fnm, emailid, pwd)

        if len(pwd) < 3:
            messages.error(request, 'Password must be more than three character')
            return redirect('signn.html')
        
        get_all_user_by_username = User.objects.filter(username=fnm)
        if get_all_user_by_username:
            messages.error(request, 'Entered username already exsits')
            return redirect('signn.html')

        sign_user=User.objects.create_user(fnm, emailid, pwd)
        sign_user.save()
        return redirect('loginn.html')
    return render(request, 'signn.html')

def loginn(request):
    if request.method=="POST":
        fnm=request.POST.get('fnm')
        pwd=request.POST.get('pwd')
        print(fnm, pwd)
        login_user = authenticate(username=fnm, password=pwd)
        if login_user is not None:
            login(request, login_user)
            return redirect('todopath.html')
        else:
            messages.error(request, 'user does not exsit, create an account')
            return redirect('signn.html')
        
    return render(request, 'loginn.html')

def todopath(request):
    if request.method=='POST':
        title=request.POST.get('title')
        print(title)
        todo_method=models.TODOTASK(task_name=title, user=request.user)
        todo_method.save()

    all_todos = TODOTASK.objects.filter(user=request.user)
    context = {
        'todos':all_todos
    }
    return render(request, 'todopath.html', context)

def DeleteTask(request, name):
    get_task = TODOTASK.objects.get(user=request.user, task_name=name)
    get_task.delete()
    return redirect('todopath.html')

def UpdateTask(request, name):
    get_task = TODOTASK.objects.get(user=request.user, task_name=name)
    get_task.status = True
    get_task.save()
    return redirect('todopath.html')