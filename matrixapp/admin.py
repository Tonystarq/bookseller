from ast import Add
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import *


# Register your models here.

# class UserModel(UserAdmin):
#     list_display = ['username', 'user_type']


# class UserModel(UserAdmin):
#     pass

admin.site.register(CustomUser)
admin.site.register(SuperAgent)
admin.site.register(HOD)

admin.site.register(Customer)
admin.site.register(BuyBook)
admin.site.register(AddBook)

