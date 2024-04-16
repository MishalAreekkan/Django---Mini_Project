from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import Vehicleform
# Create your views here.

def admins(request):
    if request.POST:
        uname= request.POST["username"]
        em=request.POST["email"]
        passw = request.POST["password"]
        cnpass= request.POST["conpassword"]
        if len(uname)<4:
            return HttpResponse("name shaoud have 4 letters")
        if not uname.isalpha():
            return HttpResponse("name should n't contain number")
        if len(passw)<2:
            return HttpResponse("password should contain minimum 4 characters")
        if passw == cnpass:
            User.objects.create_user(username=uname,password=passw,email=em)
            return render(request,"login.html")
    return render(request,"admin.html")

def user_login(request):
    if request.method == "POST":
        log_name = request.POST["user_name"]
        log_pass = request.POST["pass_word"]
        user = authenticate(username = log_name,password = log_pass)
        if user:
            login(request,user)
            return redirect("home")
    return render(request,"login.html")

def user_logout(request):
    logout(request)

@login_required(login_url="login")
def home(request):
    obj = Vehicleform()
    return render(request,"home.html",{"dict":obj})


