# -*- encoding: utf-8 -*-


from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm
from django.contrib import messages
from app import views
from .models import *

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None and user.is_staff is True:
                login(request, user)
                return redirect("/index/")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})

def register_user(request):

    msg     = None
    success = False

    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            messages.success(request, 'Account is created for ' + username)
            return redirect("loginCustomer/")
            
        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })


# --------------------------------------Customer login------------------------------------------
def loginCustomer(request):
    msg = None
    check_user = None
    user= None
    try:
        if request.method == "POST":
            username = request.POST.get('username')
            check_user = User.objects.filter(username=username).first()
            print(check_user)
            if check_user:
                # pk = check_user.values_list('pk', flat=True)
                # user = check_user[0]
                user = User.objects.get(id = check_user.id)
                login(request , user)
                return redirect('/customerHome/')
            else:
                msg = 'Error validating the form'
        else:
            print('Error')
    except Exception as e:
        print(e)
    context = {'user':user, "msg" : msg}

    return render(request, "accounts/loginCustomer.html", context)