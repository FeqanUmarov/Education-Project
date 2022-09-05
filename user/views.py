import email
from django import forms
import django
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentSignUp, LoginForm, UserProfile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.db import transaction
from .models import Course, Student, User
from course.models import CourseApply

# Create your views here.
@transaction.atomic
def register(request):


    form = StudentSignUp(request.POST or None, request.FILES or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user = user)
        student.university = form.cleaned_data.get('university')

        student.save()

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
    messages.success(request, "Ugurla cixis etdiniz")
    return redirect("index")


def myprofile(request,id):
    profile = get_object_or_404(User,id=id)
    if profile.is_course == True:
        course_apply = CourseApply.objects.filter(user_id = id).first()
    elif profile.is_student == True:
        course_apply = CourseApply.objects.filter(current_student = id).first()
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


