from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import transaction
from django.forms import inlineformset_factory
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import *
from authentication.models import *
from authentication.forms import SignUpForm


# --------------------------Customer related----------------------------
class CustomerForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Name",                
                "class": "form-control"
            }
        ))

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password1",                
                "class": "form-control"
            }
        ))

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password2",                
                "class": "form-control"
            }
        ))
    
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    phone = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Phone Number",                
                "class": "form-control"
            }
        ))
    addressline1 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Address Line1",                
                "class": "form-control"
            }
        ))
    addressline2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Address Line2",                
                "class": "form-control"
            }
        ))
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "City",                
                "class": "form-control"
            }
        ))
    pincode = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Pincode",                
                "class": "form-control"
            }
        ))
    # is_staff = forms.BooleanField(initial=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone', 'addressline1', 'addressline2', 'city', 'pincode', 'is_active']
        exclude = ['user', 'groups', 'user_permissions', 'is_superuser', 'last_login', 'is_staff', 'date_joined']

Customerformset = inlineformset_factory(User, Customer, 
    fields=('Account_Number', 'STB_Number', 'Area_Name', 'NODE_Number', 'Bank_Account', 'IFSC_code', 'is_active'), extra=1, 
    can_delete=False) 


# --------------------------Operator related-----------------------------------------
class OperatorForm(UserCreationForm):
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Name",                
                "class": "form-control"
            }
        ))

    
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    phone = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Phone Number",                
                "class": "form-control"
            }
        ))
    addressline1 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Address Line1",                
                "class": "form-control"
            }
        ))
    addressline2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Address Line2",                
                "class": "form-control"
            }
        ))
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "City",                
                "class": "form-control"
            }
        ))
    pincode = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Pincode",                
                "class": "form-control"
            }
        ))
    
    is_staff = forms.BooleanField(initial=True)
    password1 = forms.CharField(widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password1",                
                "class": "form-control",
                "value": "admin123@@",
                "disabled": True
            }
        ))
    password2 = forms.CharField(widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password2",                
                "class": "form-control",
                "value": "admin123@@",
                "disabled": True
            }
        ))
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',  'phone', 'addressline1', 'addressline2', 'city', 'pincode', 'is_active', 'is_staff' ]
        
        
        # exclude = ['password', 'password1', 'password2','user', 'groups', 'user_permissions', 'is_superuser', 'last_login', 'is_staff', 'date_joined']

Operatorformset = inlineformset_factory(User, Operator, 
    fields=('Area', 'Pan_Number', 'Bank_Account', 'IFSC_code'), extra=1, 
    can_delete=False) 



class CreatePlansForm(ModelForm):
    Name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Plan Name",                
                "class": "form-control"
            }
        ))
    
    Plan_ID = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Plan ID",                
                "class": "form-control"
            }
        ))
    
    validity = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Validity",                
                "class": "form-control"
            }
        ))

    price = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Price ₹",                
                "class": "form-control"
            }
        ))

    company_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Company Name",                
                "class": "form-control"
            }
        ))

    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Description",                
                "class": "form-control"
            }
        ))

    speed = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Speed Line1",                
                "class": "form-control"
            }
        ))

    data_limit = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Data Limit",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = createPlans
        fields = '__all__'
        
class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)