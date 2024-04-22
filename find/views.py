from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import Vehicleform,Searching
from .models import Vehicle_type
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
        print(user)
        if user:
            login(request,user)
            
            request.session["user_session"] = "new_user"
            return redirect("search")
    return render(request,"login.html")

def user_logout(request):
    logout(request)
    return redirect("login")

def home(request):
    l = request.GET.get("owner")
    print(l)
    form = Vehicleform(request.POST,request.FILES)
    if request.method == 'POST':
        print(form)
        if form.is_valid():
            name = form.cleaned_data['name']
            register_no = form.cleaned_data['register_no']
            owner = form.cleaned_data['owner']
            model = form.cleaned_data['model']
            image = form.cleaned_data['image']
            notes = form.cleaned_data['notes']
            print(name,register_no,owner,model,image,notes)
            form.save()
            return redirect('homelist')
    return render(request,"home.html",{"dict":form})

@login_required(login_url="login")
def searching(request):
    form = Searching() 
    vehicles = None
    if request.method == "POST":
        form = Searching(request.POST)
        if form.is_valid():
            data = form.cleaned_data['search']
            vehicles = Vehicle_type.objects.filter(register_no=data)
            
    return render(request,"search.html",{'form':form,'vehicles':vehicles})

# def home_list(reqeust):
#     # message = "hello {} how are you".format(q)
#     data = Vehicle_type.objects.all()
#     context = {
#         "data":data,
#     }
#     # print(Vehicle_type.objects.get(owner = "maiz"))
#     return render(reqeust,"home_list.html",context)

def deleting(request,id):
    deleted_one = Vehicle_type.objects.get(id=id)
    deleted_one.delete()
    return redirect("homelist")

# def editing(request,id):
#     edited_one = Vehicle_type.objects.get(id=id)
#     form = Vehicleform(request.POST,instance= edited_one)
#     if form.is_valid():
#         edited_one.save()
#         return redirect("/homelist")
#     form = Vehicleform(instance = edited_one)
#     return render(request,"edit.html",{"data":form})





# def qry(request):
#     q = request.GET.get("name")
#     message = "hello {} how are you".format(q)
#     return render(request,"qrys.html",{"message":message})