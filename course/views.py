from email import message
from email.policy import default
from pyexpat.errors import messages
from tkinter.messagebox import NO
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from course.models import CourseBoss, Branchs, CourseType,Comment,CoursePhoto, CourseApply, Exam, ExamApply
from user.models import Course
from user.models import User, Course, Student
from .forms import CourseInfo, CourseBranch, AddComment, CourseGallery, CourseExam, AskCourse
# Create your views here.


def courses(request):

    keyword = request.GET.get("keyword")
    if keyword:
        courses = CourseBoss.objects.filter(course_name__contains = keyword)

        return render(request,"courses.html",{"course_values":courses})

    value = CourseBoss.objects.all()




    contex = {
        "course_values":value
    }

    return render(request,"courses.html",contex)


@login_required(login_url='course/addcourse')
def addcourse(request):
    form = CourseInfo(request.POST or None,request.FILES or None,user=request.user)
    if form.is_valid():
        course = form.save(commit=False)
        course.user= request.user
        form.save()
        messages.success(request,"Kurs ugurla elave edildi")

        return redirect ("course:courses")


    contex = {
        "form": form,
    }

    return render(request,"addcourse.html", contex)


@login_required(login_url='course/addbranch')
def addbranch(request,id):
    form = CourseBranch(request.POST or None)

    if form.is_valid():
        branchs = form.save(commit=False)
        branchs.branch = CourseBoss.objects.filter(id=id).first()
        branchs.save()

        return redirect("course:detailcourse",id=id)


    contex = {
        "form": form,
    }

    return render(request,"addbranch.html", contex)

@login_required(login_url='course/addexam')
def addexam(request,id):
    form = CourseExam(request.POST or None)

    if form.is_valid():
        exam = form.save(commit=False)
        exam.course = get_object_or_404(CourseBoss,id=id)
        exam.save()

        return redirect("course:detailcourse",id=id)


    contex = {
        "form": form,
    }

    return render(request,"addexam.html", contex)


def courseexam(request,id):
    course_exam = Exam.objects.filter(course=id)
    contex={
        "course_exams":course_exam
    }
    return render (request,"tests.html",contex)

@login_required(login_url='course/tests')
def tests(request):
    tests = Exam.objects.all()
    contex = {
        "tests": tests,
    }
    return render(request,"tests.html",contex)

@login_required(login_url='course/courseapply')
def courseapply(request,id):
    form = AskCourse(request.POST or None)

    if form.is_valid():
        apply = form.save(commit=False)
        user_id = CourseBoss.objects.get(id=id).user_id
        apply.current_student = request.user.id
        apply.user = User.objects.filter(id=user_id).first()
        apply.course = CourseBoss.objects.filter(id=id).first()
        apply.save()

        return redirect("course:detailcourse",id=id)


    contex = {
        "form": form,
    }

    return render(request,"courseapply.html", contex)

@login_required(login_url='course/coursenotification')
def coursenotification(request,id):

    student_info = CourseApply.objects.filter(course_id=id)
    notification_common = CourseApply.objects.all()

    contex = {
        "student_infos": student_info,
        "notification_commons":notification_common
    }


    return render(request,"coursenotification.html",contex)

@login_required(login_url='course/commonnotification')
def commonnotification(request):


    notification_common = CourseApply.objects.all()
    courses = CourseBoss.objects.all()

    contex = {

        "notification_commons":notification_common,
        "courses":courses

    }


    return render(request,"commonnotification.html",contex)




@login_required(login_url='course/addphoto')
def addphoto(request,id):
    form = CourseGallery(request.POST or None, request.FILES or None)

    if form.is_valid():
        course_photo = form.save(commit=False)
        course_photo.course = CourseBoss.objects.filter(id=id).first()
        course_photo.save()
        return redirect("course:detailcourse",id=id)


    contex = {
        "form": form,
    }

    return render(request,"addphoto.html", contex)

def detailcourse(request,id):
    course = CourseBoss.objects.filter(id=id).first()
    course_branch = Branchs.objects.filter(branch_id=id)
    course_apply = CourseApply.objects.filter(course_id = id)
    course_type = CourseType.objects.filter(id=id)
    form = AddComment()
    comments = course.comments.all()
    contex = {
        "course_values":course,
        "course_branch":course_branch,
        "course_type":course_type,
        "comments":comments,
        "courseapply":course_apply,
        "form":form,
    }
    return render(request, "detailcourse.html",contex)

def updatecourse(request,id):
    course = get_object_or_404(CourseBoss,id=id)
    form = CourseInfo(request.POST or None ,user=request.user, instance=course)
    if form.is_valid():
        course = form.save(commit=False)
        course.user = request.user
        course.save()

        messages.success(request,"Kurs ugurla yenilendi")

        return redirect ("course:detailcourse",id=id)

    contex = {
        "form":form,

    }

    return render(request, "updatecourse.html",contex)

def applyexam(request,id):
    apply_exam = ExamApply()
    exam_data = Exam()

    if request.method == "POST":
        apply_exam.student_name = request.user.name
        apply_exam.student_surname = request.user.surname
        apply_exam.student_email = request.user.email
        apply_exam.course = CourseBoss.objects.filter(id=id).first()
        apply_exam.exam = Exam.objects.get(course_id=id)
        #exam_data.empyt_space = int((Exam.objects.get(course_id=id).empty_space))-1
        #empty_data_last = int(empty_data)-1
        #exam_data.empty_space = empty_data_last
        #new_empty_data = Exam.objects.get(course_id=id).empty_space
        #new_empty_data = empty_data_last
        exam_data.save()
        apply_exam.save()

        return redirect ("course:courses")




    return render(request,"applyexam.html")









def deletecourse(request,id):
    course = get_object_or_404(CourseBoss,id=id)
    course.delete()
    return redirect("course:courses")

def updatebranch(request,id):
    branch = get_object_or_404(Branchs,id=id)
    form = CourseBranch(request.POST or None, instance=branch)
    if form.is_valid():
        branch = form.save(commit=False)
        branch.save()

        return redirect("course:courses")


    contex = {
        "form":form,
        "branch":branch

    }

    return render(request, "updatebranch.html",contex)

def comment(request,id):
    course = get_object_or_404(CourseBoss,id=id)

    form = AddComment(request.POST or None)

    if form.is_valid():
        addcomment = form.save(commit=False)
        addcomment.comment_author = request.user
        addcomment.course = get_object_or_404(CourseBoss,id=id)
        addcomment.save()

        return redirect("course:detailcourse",id=id)

def gallery(request,id):
    photo = CoursePhoto.objects.filter(course_id=id)

    contex = {
        "photo_gallerys":photo,
    }

    return render (request,"photogallery.html",contex)

def confirm(request, id):
    status = CourseApply.objects.filter(id=id).first()
    status.confirm = 1
    status.pending = 0
    status.cancel = 0
    status.save()
    return redirect("course:commonnotification")

def cancel(request,id):
    status = CourseApply.objects.filter(id=id).first()
    status.confirm = 0
    status.pending = 0
    status.cancel = 1
    status.save()
    return redirect("course:commonnotification")



def delete(request,id):
    status = get_object_or_404(CourseApply,id=id)
    status.delete()
    return redirect("course:courses")










