# -*- encoding: utf-8 -*-


from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Operator)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(STB)
admin.site.register(Node)
admin.site.register(PaymentDetails)
admin.site.register(CollectionAgent)
admin.site.register(ServiceRequest)

