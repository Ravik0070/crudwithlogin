from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from todo.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from todo.models import Todos

from django.urls import reverse

#--------------------------------Home
@login_required(login_url='/login/')
def home(request):
    data = Todos.objects.filter(owner=request.user.pk)
    context = {
        'data':data
    }
    return render(request,'home.html',context)

#------------------------------------------Add todo
def addtodo(request):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['description']
        completed = request.POST['is_completed']
        if completed == "on":
            completed = True
        else:
            completed = False
        add = Todos(owner=request.user,title=title,description=desc,is_completed=completed)
        add.save()
        return HttpResponseRedirect(reverse('home'))
    else:
        return render(request,"addtodo.html")

def viewtodo(request,id):
    data = Todos.objects.get(id=id)
    context = {
        "data":data
    }
    return render(request,"viewtodo.html",context)

#------------------------------------------edit todo
def edittodo(request,id):
    data = Todos.objects.get(id=id)
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['description']
        completed = request.POST.get('is_completed',False)
        if completed == "on":
            completed = True
        else:
            completed = False
        data.title = title
        data.description = desc
        data.is_completed = completed
        data.save()
        return HttpResponseRedirect(reverse('home'))
    context = {
        "data":data
    }
    return render(request,"edittodo.html",context)

#------------------------------------------delete todo
def deletetodo(request,id):
    data  = Todos.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect(reverse('home'))


#--------------------------------Register
def register(request):
    if not  request.user.is_authenticated:
        if request.method == "POST":
            form = SignupForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password1")
                form.save()
                new_user = authenticate(username=username,password=password)
                if new_user is not None:
                    login(request,new_user)
                    return render(request,"home.html")
        else:
            form = SignupForm()
        return render(request,'register.html',{'form':form})
    else:
        return HttpResponseRedirect(reverse('home'))

#---------------------------------login
def loggin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username =  form.cleaned_data['username']
                password =  form.cleaned_data['password']
                new_user = authenticate(username=username,password=password)
                if new_user is not None:
                    login(request,new_user)
                    return HttpResponseRedirect(reverse('home'))
        else:
            form = AuthenticationForm()
            return render(request,'login.html',{"form":form})
    else:
        return HttpResponseRedirect(reverse('home'))
        
#----------------------------------logout
@login_required(login_url='/login/')
def loggout(request):
    if request.user:
        logout(request)
        return HttpResponseRedirect(reverse('loggin'))

