from django.contrib import admin
from .models import User, Course, Student, Tutor
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UserFeild(UserAdmin):
    fieldsets = (
    (None, {'fields': ('is_course','is_student','is_teacher','name','surname','username','email','user_profile','password')}),
)

admin.site.register(User, UserFeild)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Tutor)
