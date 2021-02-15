# -*- encoding: utf-8 -*-


from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.home, name='home'),

    # The index page
    path('index/', views.index, name='index'),

    # for admin and operators only
    path('index/customers/', views.customers, name="customers"),
    path('index/operators/', views.operators, name="operators"),
    path('employees/', views.employees, name="employees"),
    path('payments/', views.payments, name="payments"),
    path('serviceRequests/', views.serviceRequests, name="serviceRequests"),
    path('stb/', views.stb, name="STB"),
    path('createPlans/', views.createPlans, name="createPlans"),

    path('testing/', views.testing, name='testing'),

    # registeration urls
    path('newCustomer/', views.newCustomer, name='newCustomer'),                   #Creates new cutomer
    path('updateCustomer/<str:id>/', views.updateCustomer, name='updateCustomer'), #Updates cutomer
    path('newOperator/', views.newOperator, name='newOperator'),                   #Creates new operator
    path('updateOperator/<str:pk>/', views.updateOperator, name='updateOperator'), #Updates operator
    path('addEmployees/', views.addEmployees, name='addEmployees'), #Creates Employees

    # for customers
    path('customerHome/', views.customerHome, name='customerHome'),
    path('customerTickets/', views.customerTickets, name='customerTickets'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
