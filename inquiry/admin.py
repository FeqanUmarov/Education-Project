from django.contrib import admin
from .models import UserQuery, TutorQuery

# Register your models here.
admin.site.register(UserQuery)
admin.site.register(TutorQuery)