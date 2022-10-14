from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from .forms import LoginForm, UserProfile, UserSignUp,Approve
from .models import User
from course.models import CourseApply
from django.core.mail import EmailMessage
import random


# Create your views here.
@transaction.atomic
def register(request):

    form = UserSignUp(request.POST or None, request.FILES or None)
    if form.is_valid():
        global user
        user = form.save(commit=False)
       
        #messages.success(request,"Uğurla qeydiyyatdan keçdiniz!")
        return redirect("user:applyregister") 
        #return redirect("user:applyregister", request,number,user)

    contex = {
        "form": form
    }
    return render(request, "register.html", contex)


def applyregister(request):
    number = random.randint(1111,9999)
    email = EmailMessage(
    'Dogrulama',
    str(number),
    settings.EMAIL_HOST_USER,
    [str(user.email)]   
    )
    email.fail_silently = False
    email.send()
    form = Approve(request.POST or None)
    if form.is_valid():
        code = form.cleaned_data.get("approvecode")
        if str(number)==str(code):
            user.save()
            messages.success(request,"Uğurla qeydiyyatdan keçdiniz!")
            return redirect("index")
            
        else:
            messages.success(request,"Dogru kodu daxil edin")

    
    contex = {
        "form": form
        }
    return render(request,"approve.html",contex)


def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        user = User.objects.filter(email=email)
        if user.exists():
            user = authenticate(
                username=user.first().username, password=password)
            if user:
                login(request, user)
                messages.success(request, "Uğurla giriş etdiniz")
                return redirect("index")
            else:
                messages.success(request, "Parol yanlışdır")

                return render(request, "login.html", context)
            
        elif not user.exists():
                messages.success(request, "Email yanlışdır")
                return render(request, "login.html", context)
                
            
            
        

        
        

        

    return render(request, "login.html", context)


def logoutUser(request):
    logout(request)
    messages.success(request, "Uğurla çıxış etdiniz")
    return redirect("index")


def myprofile(request, id):
    profile = get_object_or_404(User, id=id)

    course_apply = CourseApply.objects.filter(user_id=id).first()

    form = UserProfile(request.POST or None,
                       request.FILES or None, instance=profile)

    if form.is_valid():
        profile = form.save(commit=False)
        profile.save()

        return redirect("user:myprofile", id=id)

    contex = {
        "form": form,
        "userprofile": profile,
        "course_apply": course_apply,
    }

    return render(request, "myprofile.html", contex)
