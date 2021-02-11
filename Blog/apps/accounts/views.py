
from django.db.models.fields import EmailField
from django.shortcuts import redirect, render
from django.http import request as r
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from .models import UserProfile

# Create your views here.
def user_logout(r):
    logout(r);
    return redirect('/');

def check_for_existing_user(email, username):
    all_user = User.objects;
    return all_user.filter(username=username).exists() or all_user.filter(email=email).exists();

def register_user(r):
    context={
        'site_name' : 'Blog',
    };

    if r.method == 'POST':
        print("POST METHOD")
        username = r.POST["username"]
        email = r.POST["email"]
        password1 = r.POST["password1"]
        password2 = r.POST["password2"]

        context["username"] = username;
        context["email"] = email;
        context["password1"] = password1;
        context["password2"] = password2;

        if check_for_existing_user(email,username):
            context["error"] = "UserName or EmailId already exists";
            return render(r, "register.html", context);
        else:
            UserProfile.register(email=email,username=username,password=password1);
            return redirect('/');
    else:
        return render(r, "register.html", context);

def is_user_send_email(email : str):
    return "@gmail.com" in str(email)

def login_user(r):

    context = {
        'site_name' : 'Blog'
    };

    #looking for Post method
    if r.method == 'POST':
        
        username = r.POST["username"]
        password = r.POST["password"] 

        #checking if user pass email id or not
        if is_user_send_email(username):
            print("User Send Email address");
            ## checking for if the email id already present in the data base or not
            if  User.objects.filter(email=username).exists():
                username = User.objects.get(email=username).username;
            else:
                context["error"] = "Email or Password is wrong";
                return render(r, "login.html", context);
       
        user = authenticate(r, username=username, password=password);

        if user is not None:
            print("User Found");
            login(r, user);
            return redirect('/');
        else:
            context["error"] = "Email or Password is wrong";
    
    return render(r, "login.html", context);
        