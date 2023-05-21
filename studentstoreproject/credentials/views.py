
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from credentials.models import Department,Courses
from django.contrib import messages


# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("newform")
        else:
            messages.info(request, "invalid credentials")
            return redirect("login")
    return render(request, "login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def newform(request):
    if request.method == 'POST':
        username = request.POST['username']
        dateofbirth = request.POST['dateofbirth']
        age = request.POST['age']
        gender = request.POST['gender']
        phoneno = request.POST['phoneno']
        mailid = request.POST['mailid']
        address = request.POST['address']
        department = request.POST['department']
        courses = request.POST['courses']
        purpose = request.POST['purpose']
        messages.success(request, "Your profile was updated.")




        print("user created")

        return redirect("newform")
    return render(request, "newform.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"USERNAME TAKEN")
                return redirect("register")
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request,"EMAIL TAKEN")
            #     return redirect("register")
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                print("user created")
                return redirect("login")
        else:
            messages.info(request, "password is not matching")
            print("password is not matching")
        return redirect('/')
    return render(request,"register.html")