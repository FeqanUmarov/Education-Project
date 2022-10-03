from django.contrib import admin
from django.urls import path
from inquiry import views

app_name = "inquiry"

urlpatterns = [
    path('inquirys/', views.inquirys, name = "inquirys"),
    
    path('teacherquery/', views.teacherquery, name = "teacherquery"),

]