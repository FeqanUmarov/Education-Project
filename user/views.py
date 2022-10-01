import email
from django import forms
import django
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserSignUp, LoginForm, UserProfile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.db import transaction
from .models import User
from course.models import CourseApply, CourseBoss

# Create your views here.
@transaction.atomic
def register(request):

    form = UserSignUp(request.POST or None, request.FILES or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        messages.success(request,"Uğurla qeydiyyatdan keçdiniz!")

        return redirect("index")

    contex = {
        "form": form
        }
    return render(request,"register.html", contex)

def loginUser(request):
    form = LoginForm(request.POST or None)
    context ={
        "form":form
     }

    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        user = User.objects.get(email=email).username

        user = authenticate(username = user,password = password)

        if user is None:
            messages.success(request,"İstifadəçi mövcud deyil")

            return render(request, "login.html", context)



        messages.success(request,"Uğurla giriş etdiniz")
       
        login(request, user)
        return redirect("index")

    return render(request,"login.html",context)



def logoutUser(request):
    logout(request)
    messages.success(request, "Uğurla çıxış etdiniz")
    return redirect("index")


def myprofile(request,id):
    profile = get_object_or_404(User,id=id)

    course_apply = CourseApply.objects.filter(user_id = id).first()
   
    form = UserProfile(request.POST or None, request.FILES or None, instance=profile)



    if form.is_valid():
        profile = form.save(commit=False)
        profile.save()

        return redirect("user:myprofile",id=id)



    contex = {
        "form":form,
        "userprofile":profile,
        "course_apply":course_apply,
    }

    return render(request, "myprofile.html", contex)





