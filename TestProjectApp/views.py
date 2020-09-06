from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Project
from django.contrib.auth.hashers import make_password, check_password
import random
import string
from django.contrib.auth import logout,login,authenticate
from django.db import IntegrityError

def __encrypt_password(password):
    
    ep = make_password(password)
    
    return ep


def __get_or_generate_login_id(UniqueID):
    if len(UniqueID) == 0:
        letters = string.ascii_lowercase
        UniqueID = ''.join(random.choice(letters) for i in range(6))
    return UniqueID

# Create your views here.
def signupuser(request):

    
    if request.method == 'GET':
        return render(request,'project/signupuser.html')
        
       #user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])

    try:
        if request.method == 'POST':
            fname = request.POST['fname']
            lname = request.POST['lname']
            Image = request.POST['Image']
            LoginID = __get_or_generate_login_id(request.POST['UniqueID'])
            EmailID = request.POST['EmailID']
            Password = __encrypt_password(request.POST['Password'])
            Age = request.POST['Age']
                #Project.objects.create(fname, lname, age, LoginID, EmailID, Password)
            user = Project.objects.create(fname= fname, lname = lname, Age = Age, LoginID = LoginID, EmailID = EmailID, Password = Password)
            user.save()

            
            #login(request)
            return redirect('page') #pass name where it should go 

    except IntegrityError as e:
        print(e)
        g = str(e)
        st = g.split(".")
        new = st[1]
        return render(request,'project/signupuser.html',{'error': new + ' already exist, please use a different one!'})



def page(request):
    return render(request,'project/page.html')




    #Login Users Page
def login(request):

    if request.method == 'POST':
        #user = authenticate(request, EmailID=request.POST['EmailID'], Password=__encrypt_password(request.POST['Password']))
        user = Project.objects.get(EmailID=request.POST['EmailID'])
       
    
        
        if user is None or not check_password(request.POST['Password'],user.Password):
           
            return render(request, 'project/login.html')
        else:
          
            request.session["email"]=request.POST['EmailID']
            print("Session in login: " + str(request.session["email"]))
            return redirect('final')
    else:

            return render(request, 'project/login.html')



###For logout Function
def LogOut(request):
    if request.method == "POST":
        #logout() is a in inbuilt function which will actually fush the session, you can check in __init__.py
        logout(request)
        return redirect("signupuser")



def final(request):
    print("Session ",str(request.session))
    print("Email ID: " + str(request.session["email"]))
    user_details = Project.objects.get(EmailID=request.session["email"])

    
    return render(request, 'project/final.html', {'user_details' : user_details})


