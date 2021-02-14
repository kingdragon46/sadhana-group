# -*- encoding: utf-8 -*-


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from authentication.models import User
from .forms import *
from .models import *
from authentication.forms import SignUpForm
from django.forms import inlineformset_factory


def home(request):
    
    context = {}
    context['segment'] = 'home'

    html_template = loader.get_template( 'home.html' )
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))


# ----------------------------------------------Admin & Operator views------------------------------------------------------------

def users(request):
    users = User.objects.all().filter(is_staff=False)
    print(users)
    context = {'users':users}
    html_template = loader.get_template( 'ui-breadcrumb-pagination.html' )
    return HttpResponse(html_template.render(context, request))

def operators(request):
    users = User.objects.all().filter(is_staff=True, is_superuser=False)
    print(users)
    context = {'users':users}
    html_template = loader.get_template( 'operator.html' )
    return HttpResponse(html_template.render(context, request))



def testing(request):
    print(request.user)
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    print(form)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=cust)       
        if form.is_valid():
            form.save()

    context = {'form':form}       
    html_template = loader.get_template( 'testing.html')
    return HttpResponse(html_template.render(context, request))



def newCustomer(request):
    msg     = None
    success = False
    try:
        form = CustomerForm()
        form2 = Customerformset()
        if request.method == 'POST':
            print(request.POST)
            form = CustomerForm(request.POST)
            if form.is_valid():
                form = form.save()
                form2 = Customerformset(request.POST, instance=form)
                if form2.is_valid:
                   form2.save()
                   return redirect('users')              
                messages.success(request, 'Account is created for ' + username)
                
            else:
                msg = 'Form is not valid'    
        else:
            form = CustomerForm()
            form2 = Customerformset(instance=user)
    except Exception as e:
        print (e)
    context = {"form": form, "form2": form2, "msg" : msg, "success" : success }

    html_template = loader.get_template( 'accounts/newCustomer.html')
    return HttpResponse(html_template.render(context, request))

def newOperator(request):
    msg     = None
    success = False
    try:
        form = OperatorForm()
        form2 = Operatorformset()
        if request.method == 'POST':
            
            print(request.POST)
            
            form = OperatorForm(request.POST)
            # print(form)
            if form.is_valid():
                form = form.save()
                print(form)               
                form2 = Operatorformset(request.POST, instance=form)
                if form2.is_valid:
                   form2.save()
                   print(form2)
                   return redirect('operators')
                messages.success(request, 'Account is created for ' + username)
                
            else:
                msg = 'Form is not valid'    
        else:
            form = OperatorForm()
            form2 = Operatorformset(instance=user)
    except Exception as e:
        print (e)
    context = {"form": form, "form2": form2, "msg" : msg, "success" : success }

    html_template = loader.get_template( 'accounts/newOperator.html')
    return HttpResponse(html_template.render(context, request))


def createPlans(request):
    try: 
        if request.method == 'GET':
            form = CreatePlansForm()
        else:
            form = CreatePlansForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                    msg = 'Form is not valid'         
    except Exception as e:
        print (e)
    context = {"form":form}
    html_template = loader.get_template( 'createPlans.html')
    return HttpResponse(html_template.render(context, request))

# --------------------------------------Customer Views----------------------------------------------

def customerHome(request):

    context={}

    html_template = loader.get_template( 'accounts/customer_home.html')
    return HttpResponse(html_template.render(context, request))


def customerTickets(request):

    context={}

    html_template = loader.get_template( 'tickets.html')
    return HttpResponse(html_template.render(context, request))