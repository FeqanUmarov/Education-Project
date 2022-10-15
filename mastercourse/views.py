from django.shortcuts import render, redirect
from django.contrib import messages
from course.models import CourseBoss


def index(request):
    value = CourseBoss.objects.all()
    contex = {
        "course_values":value,
    }
    return render(request,"index.html",contex)


