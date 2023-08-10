# bankapp/admin.py
from django.contrib import admin
from .models import District,SubArea,AccountType,Customer,Materials

admin.site.register(District)
admin.site.register(SubArea)
admin.site.register(AccountType)
admin.site.register(Customer)
admin.site.register(Materials)
from django.contrib import admin

# Register your models here.
