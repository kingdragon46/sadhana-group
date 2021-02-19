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


Type_choices = ( 
                    ("1", "Prepaid"), 
                    ("2", "Postpaid"), 
                    ("3", "Complementary"),
                )

Status_choices = (
    ("1","Active"),
    ("2","Inactive"),
)

Box_choices = ( 
                    ("1", "SD"), 
                    ("2", "HD"), 
                    ("3", "HD+"),
                    ("4", "Other"),
                )

class STB(models.Model):
    serial_number = models.CharField(_("Serial Number"), max_length=50, null=True)
    issue_date = models.DateField(_("Issue Date"), auto_now=False, auto_now_add=False)
    DOP = models.DateField(_("Date Of Purchase"), auto_now=False, auto_now_add=False)
    Type = models.CharField(_("Type"), max_length=50, null=True, choices = Type_choices, default = '1')
    status = models.CharField(_("Status"), max_length=50, choices = Status_choices, default = '1')
    box_type = models.CharField(_("Box Type"), max_length=50, choices = Status_choices, default = '1')
    remark = models.TextField(_("Remark"), null=True, blank=True)
    model_number = models.CharField(_("Model Number"), max_length=50, null=True)
    is_assigned = models.BooleanField(_("Assigned"), default=False)
    user_id = models.CharField(_("User ID"), max_length=50, null=True)

    def __str__(self):
        return f'{self.serial_number}'

class Node(models.Model):
    serial_number = models.CharField(_("Serial Number"), max_length=50, null=True)
    issue_date = models.DateField(_("Issue Date"), auto_now=False, auto_now_add=False)
    DOP = models.DateField(_("Date Of Purchase"), auto_now=False, auto_now_add=False)
    STB_count = models.IntegerField(_("STB Count"))
    status = models.CharField(_("Status"), max_length=50, choices = Status_choices, default = '1')
    operator_name = models.ForeignKey(Operator, verbose_name=_("Operator Name"), on_delete=models.SET_NULL, null=True, blank=True)
    remark = models.TextField(_("Remark"), null=True, blank=True)
    model_number = models.CharField(_("Model Number"), max_length=50, null=True)


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    Account_Number = models.CharField(max_length=20, null=True)
    STB_Number = models.ForeignKey(STB, on_delete=models.PROTECT, null=True)
    Area_Name = models.CharField(max_length=100, null=True)
    NODE_Number = models.ForeignKey(Node, on_delete=models.PROTECT, null=True)
    Bank_Account = models.CharField(max_length=20, null=True)
    IFSC_code = models.CharField(max_length=20, null=True)
    is_active = models.BooleanField(default=1)

    USERNAME_FIELD= ('user')

    def __str__(self):
        return f'{self.user}'


class PaymentDetails(models.Model):
    customer_name = models.CharField(_("Customer Name"), max_length=50, null=True)
    stb_number = models.ForeignKey(STB, on_delete=models.PROTECT, null=True)
    plan_name = models.ForeignKey(createPlans, on_delete=models.PROTECT, null=True)
    amount = models.CharField(_("Amount"), max_length=50, null=True)
    transacton_id = models.CharField(_("Transaction ID"), max_length=50, null=True)
    transaction_datetime = models.DateTimeField(_("Date and Time"), auto_now=False, auto_now_add=False)
    status = models.CharField(_("Status"), max_length=50, null=True)
    circle_name = models.CharField(_("Circle Name"), max_length=50, null=True)

    def __str__(self):
        return f'{self.transaction_id}'
    
class CollectionAgent(models.Model):
    collector_id = models.CharField(_("Collector ID"), max_length=50, null=True)
    name = models.CharField(_("Name"), max_length=50, null=True)
    mobile = models.CharField(_("Phone"), max_length=50, null=True)
    email = models.EmailField(_("EMail"), max_length=254)
    date_of_joining = models.DateField(_("Date of Joining"), auto_now=False, auto_now_add=False)
    address = models.CharField(_("Address"), max_length=50, null=True)
    city = models.CharField(_("City"), max_length=50, null=True)
    state = models.CharField(_("State"), max_length=50, null=True)
    pincode = models.CharField(_("Pincode"), max_length=50, null=True)
    company_name = models.CharField(_("Company Name"), max_length=50, null=True)
    bank_account_number = models.CharField(_("Bank Account Number"), max_length=50, null=True)
    ifsc_code = models.CharField(_("IFSC COde"), max_length=50, null=True)
    branch_addresss = models.CharField(_("Branch Address"), max_length=50, null=True)
    branch_name = models.CharField(_("Branch Name"), max_length=50, null=True)

    def __str__(self):
        return f'{self.collector_id}'

