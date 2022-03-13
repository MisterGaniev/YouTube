from django.contrib import admin
from django.contrib.admin import ModelAdmin
from user_app.models import *

# Register your models here.

@admin.register(Account)
class Account_admin(ModelAdmin):
    pass
