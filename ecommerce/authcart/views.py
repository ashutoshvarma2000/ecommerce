from django.shortcuts import render, redirect, HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def signin(request):
    if request.method=="POST":
        username=request.POST['email'] 
        userpassword=request.POST['pass1'] 
        myuser=authenticate(username=username, password=userpassword)

        if myuser is not None:
            login(request, myuser)
            #messages.success(request, "Login Success") 
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials") 
            return redirect('/auth/signin')

    return render(request, 'signin.html')
    #return render(request, "signin.html")
    
def register(request):
    if request.method=="POST":
        email=request.POST['email'] 
        password=request.POST['pass1'] 
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request, "password is not matching")
            #return HttpResponse("password incorrect")
            return render (request, 'register.html')
        try:
            if User.objects.get(username=email): 
                messages.warning(request, "password incorrect")
                #return HttpResponse("password incorrect")
                return render (request, 'register.html')

        except Exception as identifier:
            pass
        user = User.objects.create_user(email, email, password)
        user.save()
        #return HttpResponse("user created",email)
    return render(request, 'register.html')

def handlelogout(request):
    logout(request)
    messages.info(request, "logout success")
    return redirect('/auth/signin')
