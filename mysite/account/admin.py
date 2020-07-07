from django.contrib import admin
from django.contrib.auth.admin import UserAdmin #helper class for making admin screen
from .models import Account
# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined','last_login', 'is_admin', 'is_staff')#which must be seen
    search_fields = ('email', 'username') #for search
    readonly_fields = ('date_joined', 'last_login') #which cannot be changed

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



admin.site.register(Account, AccountAdmin) 