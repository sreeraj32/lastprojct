from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Place
from .models import team
from django.contrib import messages,auth

 #Create your views here
def demo(request):
    place=Place.objects.all()
    team1=team.objects.all()

    return render(request,"index.html",{'place':place,'team1':team1})
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'INVALID INPUT')
            return redirect('login')



    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username is taken")
                return  redirect('register')
            elif User.objects.filter(email=email).exists():
                    messages.info(request, "email is taken")
                    return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save();
                return redirect('login')

                messages.info(request,"User created")
        else:
            messages.info(request,"password is not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
