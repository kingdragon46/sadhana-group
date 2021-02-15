# -*- encoding: utf-8 -*-


from django.contrib import admin
from .models import Operator, Customer, Employee

# Register your models here.

admin.site.register(Operator)
admin.site.register(Customer)
admin.site.register(Employee)


