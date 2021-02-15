# -*- encoding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Operator(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    Area = models.CharField(max_length=200, null=True)
    Pan_Number = models.CharField(max_length=20, null=True)
    Bank_Account = models.CharField(max_length=20, null=True)
    IFSC_code = models.CharField(max_length=20, null=True)
    is_active = models.BooleanField(default=1)
    is_staff = models.BooleanField(default=1)

    def __str__(self):
        return f'{self.user}'
    
class Customer(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    Account_Number = models.CharField(max_length=20, null=True)
    STB_Number = models.CharField(max_length=20, null=True)
    Area_Name = models.CharField(max_length=100, null=True)
    NODE_Number = models.CharField(max_length=20, null=True)
    Bank_Account = models.CharField(max_length=20, null=True)
    IFSC_code = models.CharField(max_length=20, null=True)
    is_active = models.BooleanField(default=1)

    USERNAME_FIELD= ('user')

    def __str__(self):
        return f'{self.user}'


class createPlans(models.Model):
    Name = models.CharField(null= True, max_length=50)
    Plan_ID = models.CharField(null= True, max_length=50)
    validity = models.CharField(null= True, max_length=50)
    price = models.CharField(null= True, max_length=50)
    company_name = models.CharField(null= True, max_length=50)
    description = models.CharField(null= True, max_length=50)
    speed = models.CharField(null= True, max_length=50)
    data_limit = models.CharField(null= True, max_length=50)


class Employee(models.Model):
    SR_No = models.CharField(_("Serial Number"), null=True, max_length=50, unique=True)
    Name = models.CharField(_("Name"), null=True, max_length=100)
    Emp_Number = models.CharField(_("Employee Number"), null=True, max_length=10)
    Mobile = RegexValidator( regex = r'^\+?1?\d{9,10}$', message ="Phone number must be entered in the format +919999999999. Up to 10 digits allowed.")
    email = models.EmailField(_("Email"), max_length=254)
    department = models.CharField(_("Department"), null=True, max_length=100)
    DOJ = models.DateField(_("Date of Joining"), auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'{self.Name}'