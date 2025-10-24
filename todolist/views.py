from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todolist import models
from todolist.models import TODOTASK
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse

def signn(request):
    if request.user.is_authenticated:
        return redirect('todopath.html')
    
    if request.method=="POST":
        fnm=request.POST.get('fnm')
        emailid=request.POST.get('emailid')
        pwd=request.POST.get('pwd')
        print(fnm, emailid, pwd)

        # this function is written to address the len of the password

        if len(pwd) <3:
            messages.error(request, 'Password must be more than three character')
            return redirect('signn.html')
        
        if len(fnm) < 5:
            messages.error(request, 'username should contain more than five character')
            return redirect('signn.html')
        
        # this function is written to address an error message when the user does'nt have an sign account

        get_all_user_by_username = User.objects.filter(username=fnm)
        if get_all_user_by_username:
            messages.error(request, 'Entered username already exsits')
            return redirect('signn.html')
        
        get_all_user_by_email = User.objects.filter(email=emailid)
        if get_all_user_by_email:
            messages.error(request, 'Entered email already exsits')
            return redirect('signn.html')

        sign_user=User.objects.create_user(fnm, emailid, pwd)
        sign_user.save()

        messages.success(request, 'user is created successfully')
        return redirect('loginn.html')
    return render(request, 'signn.html', {})

def loginn(request):
    if request.user.is_authenticated:
        return redirect('todopath.html')

    if request.method=="POST":
        fnm=request.POST.get('fnm')
        pwd=request.POST.get('pwd')
        print(fnm, pwd)
        login_user = authenticate(username=fnm, password=pwd)
        if login_user is None:
            messages.error(request, 'user does not exsit, create an new user')
            return redirect('signn.html')
        else:
            login(request, login_user)
            messages.error(request, 'hi welcome')
            return redirect('todopath.html')
        
    return render(request, 'loginn.html')

@login_required
def todopath(request):
    if request.method=='POST':
        task=request.POST.get('task')
        print(task)
        todo_method=models.TODOTASK(task_name=task, user=request.user)
        todo_method.save()

    all_todos = TODOTASK.objects.filter(user=request.user)
    context = {

        'todos':all_todos
    }
    return render(request, 'todopath.html', context)

@login_required
def DeleteTask(request, name):
    get_task = TODOTASK.objects.get(user=request.user, task_name=name)
    get_task.delete()
    return redirect('todopath.html')

@login_required
def UpdateTask(request, name):
    get_task = TODOTASK.objects.get(user=request.user, task_name=name)
    get_task.status = True
    get_task.save()
    return redirect('todopath.html')

def LogoutView(request):
    logout(request)
    return redirect('signn.html')