# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.contrib import admin
User = get_user_model()

from .forms import SignUpForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .forms import UserAdminCreationForm, UserAdminChangeForm

# from .models import PhoneOTP
# admin.site.register(PhoneOTP)


class CustomUserAdmin(BaseUserAdmin):

    add_form = SignUpForm
    # form = CustomUserChangeForm
    model = User
    list_display = ('username','email','phone', 'is_staff', 'is_active',)
    list_filter = ('username','email','phone','is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username','email', 'password', 'phone')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Address', {'fields': ('addressline1', 'addressline2', 'city', 'pincode')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email','phone', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.register(User, CustomUserAdmin)
