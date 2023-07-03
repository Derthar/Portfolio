from django.contrib import admin
from Users.models import User
from Products.admin import BasketAdmin

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name')
    inlines = (BasketAdmin, )