from django.shortcuts import render, redirect
from .forms import QueryForm,TutorQueryForm
from .models import UserQuery, TutorQuery
from django.contrib import messages
# Create your views here.
def inquirys(request):
    form = QueryForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        surname = form.cleaned_data.get("surname")
        email = form.cleaned_data.get("email")
        phone = form.cleaned_data.get("phone")
        username = form.cleaned_data.get("username")
        course_name = form.cleaned_data.get("course_name")
        course_email = form.cleaned_data.get("course_email")
        newquery = UserQuery(name = name, surname=surname,email=email,phone=phone,username = username,course_name=course_name,course_email=course_email)
        newquery.save()
        messages.success(request,"Sorgu ugurla elave edildi. Qisa zamanda sizinle elaqe saxlanilacaq")
        return redirect("index")


    contex = {
        "form":form
    }
    return render(request,"inquiry.html",contex)


def teacherquery(request):
    form = TutorQueryForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("teachername")
        surname = form.cleaned_data.get("teachersurname")
        email = form.cleaned_data.get("email")
        phone = form.cleaned_data.get("teacherphone")
        experience = form.cleaned_data.get("experience")
        study_field = form.cleaned_data.get("study_field")
        newquery = TutorQuery(teachername = name , teachersurname = surname,email=email,teacherphone = phone,experience=experience,study_field=study_field)
        newquery.save()
        messages.success(request,"Sorgu ugurla elave edildi. Qisa zamanda sizinle elaqe saxlanilacaq")
        return redirect("index")
        
        
    contex = {
        "form":form
    }
    return render(request,"tutorquery.html",contex)