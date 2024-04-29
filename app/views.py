from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'index.html')
def car(request):
    return render(request,'car.html')
def contact(request):
    if request.method=="POST":
        fname=request.POST.get("name")
        femail=request.POST.get("email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        query=contact(name=fname,email=femail,phoneNumber=phone,description=desc)
        query.save()
        messages.info(request,"Thanks for contacting us!!")
        return redirect("index.html")
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')


def handlelogin(request):
    if request.method=="POST":
        Username=request.POST.get("Uname")
        pass1=request.POST.get("pass1")
        myuser=authenticate(Uname=Username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login sucessful")
            return redirect("index.html")
        else:
            messages.error(request,"Invalid")
            return redirect("index.html")

    return render(request,'login.html')


def handlesignup(request):
    if request.method=="POST":
        Username=request.POST.get("Uname")
        Email=request.POST.get("Email")
        password=request.POST.get("pass1")
        Confirmpassword=request.POST.get("pass2")
        #print(Username,Email,password,Confirmpassword)

        if password!=Confirmpassword:
            messages.warning(request,"Password is incorrect")
            return redirect("signup.html")
        try:
            if User.objects.get(Uname=Username):
             messages.info(request,"Username is already taken")
            return redirect("signup.html")
        except:
            pass
        try:
            if User.objects.get(Email=Email):
             messages.info(request,"Email is Taken")
            return redirect("signup.html")
        except:
            pass


        myuser=User.objects.create_user(Username,Email,password)
        myuser.save()
        messages.info(request,"Signup success please login")
        return redirect("login.html")
    return render(request,'signup.html')
    
def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Success")
 
    return redirect("index.html")
def carindex1(request):
    return render(request,"carindex1.html")
def carindex2(request):
    return render(request,"carindex2.html")
def carindex3(request):
    return render(request,"carindex3.html")
def carindex4(request):
    return render(request,"carindex4.html")
def carindex5(request):
    return render(request,"carindex5.html")
def carindex6(request):
    return render(request,"carindex6.html")
def reviews(request):
    return render(request,"reviews.html")
def service(request):
    return render(request,"service.html")