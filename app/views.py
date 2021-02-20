# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from authentication.models import User
from django.contrib.auth.models import Group
from .forms import *
from .models import *
from authentication.forms import SignUpForm
from django.forms import inlineformset_factory
import json
from .decorators import allowed_users

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


@login_required(login_url="/login/")
@allowed_users(allowed_roles=['Admin'])
def customers(request):
    users = User.objects.all().filter(is_staff=False)
    print(users)
    context = {'users':users}
    html_template = loader.get_template( 'customers.html' )
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
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



@login_required(login_url="/login/")
def newCustomer(request):
    u =User.objects.filter(groups__name='Admin')
    print(u)
    stb = STB.objects.all().filter(is_assigned=False)
    node = Node.objects.all()
    # print(stb)
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            addressline1 = request.POST.get('addressline1')
            addressline2 = request.POST.get('addressline2')
            city = request.POST.get('city')
            pincode = request.POST.get('pincode')
            Account_Number = request.POST.get('Account_Number')
            select1 = request.POST.get('select1')
            select2 = request.POST.get('select2')
            Area_Name = request.POST.get('Area_Name')
            Bank_Account = request.POST.get('Bank_Account')
            IFSC_code = request.POST.get('IFSC_code')
            # print(select)
            check_profile = User.objects.filter(email = email).first()
            if check_profile:
                context = {'message' : 'User already exists' , 'class' : 'danger' }
                return render(request,'accounts/newCustomer.html' , context)
            user = User(username=username, email=email, first_name=name, phone=phone, addressline1=addressline1, addressline2=addressline2, city=city, pincode=pincode)
            user.save()
            group = Group.objects.get(name='Customer')
            user.groups.add(group)
            check_stb = STB.objects.all().filter(serial_number=select1)
            check_node = Node.objects.all().filter(serial_number=select2)
            check_stb.update(is_assigned=True)
            print(check_stb[0])
            cust = Customer(user=user, STB_Number=check_stb[0], NODE_Number=check_node[0], Account_Number=Account_Number, Area_Name=Area_Name, Bank_Account=Bank_Account, IFSC_code=IFSC_code)
            cust.save()
            context = {'stb':stb, 'node':node, 'message' : 'Customer created successfully' , 'class' : 'success' }
            return render(request,'accounts/newCustomer.html' , context)
        else:
            print('Error')
    except Exception as e:
        print(e)
    
    context= {'stb':stb, 'node':node}

    html_template = loader.get_template( 'accounts/newCustomer.html')
    return HttpResponse(html_template.render(context, request))

    
def save_profile(request):
    stb = STB.objects.all()
    # print(stb)
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            name = request.POST.get('name')
            email = request.POST.get('email')
            select = request.POST.get('select')
            # print(select)
            user = User(username=username, email=email, first_name=name)
            user.save()
            check_stb = STB.objects.all().filter(serial_number=select)
            print(check_stb[0])
            cust = Customer(user=user, STB_Number=check_stb[0])
            cust.save()
        else:
            print('Error')
    except Exception as e:
        print(e)
    
    context= {'stb':stb}
    html_template = loader.get_template( 'accounts/profile.html')
    return HttpResponse(html_template.render(context, request))


def get_stb_by_id(request, pk):
    stb = STB.objects.get(pk=pk)
    


@login_required(login_url="/login/")
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
                form2 = Operatorformset(request.POST, instance=form)
                if form2.is_valid:
                   form2.save()
                   return redirect('operators')
                
            else:
                msg = 'Form is not valid'    
        else:
            form = OperatorForm()
            form2 = Operatorformset(instance=user)
    except Exception as e:
        print (e)
    context = {"form": form, "form2": form2, "msg" : msg }

    html_template = loader.get_template( 'accounts/newOperator.html')
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
def updateOperator(request, pk):
    user = User.objects.get(pk=pk)
    form= OperatorForm(instance= user)
    form2 = Operatorformset(instance=user)
    
    try:
        if request.method == 'POST':
            form = OperatorForm(request.POST,instance=user)
            form2 = Operatorformset(request.POST, instance=user)
            if form.is_valid() and form2.is_valid():
                form = form.save()              
                form2.save()
                
                return redirect('operators')
    except Exception as e:
        print(e)

    context = {"form": form, "form2": form2}

    html_template = loader.get_template( 'accounts/updateOperator.html')
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
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

@login_required(login_url="/loginCustomer/")
@allowed_users(allowed_roles=['Customer'])
def customerHome(request):
    cust = request.user

    
    users = Customer.objects.all().filter(user=cust)
    print(cust)
    context={"cust":cust, 'users':users}

    html_template = loader.get_template( 'accounts/customer_home.html')
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
def updateCustomer(request, id):
    user = User.objects.get(pk=id)
    form= CustomerForm(instance= user)
    form2 = Customerformset(instance= user)
    # print(form2)
    try:
        if request.method == 'POST':           
            form = CustomerForm(request.POST,instance=user)
            form2 = Customerformset(request.POST, instance=user)
            if form.is_valid() and form2.is_valid():
                form = form.save()                            
                form2.save()
                
                return redirect('customers')
    except Exception as e:
        print(e)

    context = {"form":form, "form2": form2}

    html_template = loader.get_template( 'accounts/updateCustomer.html')
    return HttpResponse(html_template.render(context, request))


def customerTickets(request):
    user = Customer.objects.all()
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            city = request.POST.get('city')
            message_box = request.POST.get('message_box')
            sr_type = request.POST.get('sr_type')
            sub_type = request.POST.get('sub_type')
            select1 = request.POST.get('select1')
            check_stb = STB.objects.all().filter(serial_number=select1)
            print(check_stb[0])
            sr = ServiceRequest(name=name, email=email, mobile=mobile, city=city, sr_type=sr_type, sub_type=sub_type, stb=check_stb[0])
            sr.save()
            context = {'stb':stb, 'message' : 'Complaint created successfully' , 'class' : 'success' }
            return render(request,'tickets.html' , context)
        else:
            print('Error')
    except Exception as e:
        print(e)
    
    context = {'user':user}

    html_template = loader.get_template( 'tickets.html')
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
def addEmployees(request):
    form= EmployeeForm()
    try:
        if request.method == 'POST':
            form = EmployeeForm(request.POST)
            if form.is_valid():
                form.save()
                # group = Group.objects.get(name='Employee')
                # groups.add(group)
                return redirect('employees')
                print('working')
            else:
                print('Form is not valid')
    except Exception as e:
        print(e)

    context={"form": form}

    html_template = loader.get_template( 'addEmployee.html')
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
def employees(request):
    users = Employee.objects.all()
    print(users)
    context = {'users':users}
    html_template = loader.get_template( 'employees.html' )
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
def payments(request):
    
    context = {}
    html_template = loader.get_template( 'payment.html' )
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
def serviceRequests(request):
    sr = ServiceRequest.objects.all()
    
    context = {'sr':sr}
    html_template = loader.get_template( 'serviceRequest.html' )
    return HttpResponse(html_template.render(context, request))

def addserviceRequests(request):
    stb = STB.objects.all()
    print(stb)
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            city = request.POST.get('city')
            message_box = request.POST.get('message_box')
            sr_type = request.POST.get('sr_type')
            sub_type = request.POST.get('sub_type')
            select1 = request.POST.get('select1')
            check_stb = STB.objects.all().filter(serial_number=select1)
            print(check_stb[0])
            sr = ServiceRequest(name=name, email=email, mobile=mobile, city=city, sr_type=sr_type, sub_type=sub_type, stb=check_stb[0])
            sr.save()
            context = {'stb':stb, 'message' : 'Complaint created successfully' , 'class' : 'success' }
            return render(request,'newServiceRequest.html' , context)
        else:
            print('Error')
    except Exception as e:
        print(e)
    
    context = {'stb':stb}
    html_template = loader.get_template( 'newServiceRequest.html' )
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
def stb(request):
    
    context = {}
    html_template = loader.get_template( 'stb.html' )
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
def addstb(request):
    form= stbForm()
    try:
        if request.method == 'POST':
            form = stbForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account is created')

            else:
                print('Form is not valid')
    except Exception as e:
        print(e)

    context={"form": form}

    html_template = loader.get_template( 'addstb.html')
    return HttpResponse(html_template.render(context, request))
