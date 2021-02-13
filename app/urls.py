# -*- encoding: utf-8 -*-


from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.home, name='home'),

    # The index page
    path('index/', views.index, name='index'),

    # for admin and operators only
    path('index/users/', views.users, name="users"),
    path('index/operators/', views.operators, name="operators"),

    path('testing/', views.testing, name='testing'),

    # registeration urls
    path('newCustomer/', views.newCustomer, name='newCustomer'),
    path('newOperator/', views.newOperator, name='newOperator'),

    # for customers
    path('customerHome/', views.customerHome, name='customerHome'),
    path('customerTickets/', views.customerTickets, name='customerTickets'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
