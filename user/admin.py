from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UserFeild(UserAdmin):
    fieldsets = (
    (None, {'fields': ('name','surname','username','email','user_profile','phone','password')}),
)

admin.site.register(User, UserFeild)
