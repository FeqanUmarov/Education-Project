from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from user.models import User

from course.forms import (AddComment, ApplyEventForm, AskCourse, AskTrainer,
                          CourseBranch, CourseExam, CourseGallery, CourseInfo,
                          CreateEvent, CreateLessonPlan, TrainerInfo, AddBlog)
from course.models import (Branchs, CourseApply, CourseBoss, CoursePhoto,
                           CourseType, Event, EventApply, Exam, ExamApply,
                           LessonPlan, Trainer, TrainerApply, CreateBlog)

# Create your views here.


def courses(request):

    keyword = request.GET.get("keyword")
    if keyword:
        courses = CourseBoss.objects.filter(course_name__contains=keyword)

        return render(request, "courses.html", {"course_values": courses})

    value = CourseBoss.objects.all()
    trainer_value = Trainer.objects.all()
    events = Event.objects.all()

    contex = {
        "course_values": value,
        "trainer_values": trainer_value,
        "events_values":events,
    }

    return render(request, "courses.html", contex)


def aboutus(request):
    return render(request, "aboutus.html")


@login_required(login_url='course/addcourse')
def addcourse(request):
    form = CourseInfo(request.POST or None, request.FILES or None)
    if form.is_valid():
        course = form.save(commit=False)
        course.user = request.user
        form.save()
        messages.success(request, "Kurs uğurla əlavə edildi. Gün ərzində yoxlanılıb təsdiq ediləcək")

        return redirect("course:courses")

    contex = {
        "form": form,
    }

    return render(request, "addcourse.html", contex)


@login_required(login_url='course/addtrainer')
def addtrainer(request):
    form = TrainerInfo(request.POST or None, request.FILES or None)
    if form.is_valid():
        trainer = form.save(commit=False)
        trainer.user = request.user
        form.save()
        messages.success(request, "Treyner olaraq qeydiyyatdan keçdiniz. Gün ərzində yoxlanılıb təsdiq ediləcək")

        return redirect("course:courses")

    contex = {
        "form": form,
    }

    return render(request, "addtrainer.html", contex)


@login_required(login_url='course/addbranch')
def addbranch(request, id):
    form = CourseBranch(request.POST or None)

    if form.is_valid():
        branchs = form.save(commit=False)
        branchs.branch = CourseBoss.objects.filter(id=id).first()
        branchs.save()
        messages.success(request, "Filial əlavə edildi")

        return redirect("course:detailcourse", id=id)

    contex = {
        "form": form,
    }

    return render(request, "addbranch.html", contex)


@login_required(login_url='course/addexam')
def addexam(request, id):
    form = CourseExam(request.POST or None)

    if form.is_valid():
        exam = form.save(commit=False)
        exam.course = get_object_or_404(CourseBoss, id=id)
        exam.save()

        return redirect("course:detailcourse", id=id)

    contex = {
        "form": form,
    }

    return render(request, "addexam.html", contex)


@login_required(login_url='course/courseexam')
def courseexam(request, id):
    course_exam = Exam.objects.filter(course=id)
    contex = {
        "course_exams": course_exam
    }
    return render(request, "tests.html", contex)


@login_required(login_url='course/tests')
def tests(request):
    tests = Exam.objects.all()
    contex = {
        "tests": tests,
    }
    return render(request, "tests.html", contex)


@login_required(login_url='course/courseapply')
def courseapply(request, id):
    form = AskCourse(request.POST or None)

    if form.is_valid():
        apply = form.save(commit=False)
        apply.user = request.user
        apply.course = CourseBoss.objects.filter(id=id).first()
        apply.save()
        messages.success(request, "Müraciətiniz göndərildi")

        return redirect("course:detailcourse", id=id)

    contex = {
        "form": form,
    }

    return render(request, "courseapply.html", contex)


@login_required(login_url='course/applytrainer')
def applytrainer(request, id):
    form = AskTrainer(request.POST or None)

    if form.is_valid():
        trainer_apply = form.save(commit=False)
        trainer_apply.user = request.user
        trainer_apply.trainer = Trainer.objects.filter(id=id).first()
        trainer_apply.save()
        messages.success(request, "Müraciətiniz göndərildi")

        return redirect("course:detailtrainers", id=id)

    contex = {
        "form": form,
    }

    return render(request, "applytrainer.html", contex)


@login_required(login_url='course/trainernotification')
def trainernotification(request, id):
    student_apply = TrainerApply.objects.filter(trainer=id)

    contex = {
        "student_applys": student_apply,
    }

    return render(request, "trainernotification.html", contex)


@login_required(login_url='course/trainerapplynotification')
def trainerapplynotification(request, id):
    student_infos = TrainerApply.objects.filter(trainer=id)

    contex = {
        "student_infos": student_infos

    }

    return render(request, "trainerapplynotification.html", contex)


@login_required(login_url='course/coursenotification')
def coursenotification(request, id):

    student_info = CourseApply.objects.filter(course_id=id)

    contex = {
        "student_infos": student_info,
    }

    return render(request, "coursenotification.html", contex)


@login_required(login_url='course/courseapplynotification')
def courseapplynotification(request, id):

    student_info = CourseApply.objects.filter(course_id=id)

    contex = {
        "student_infos": student_info,

    }

    return render(request, "courseapplynotification.html", contex)


@login_required(login_url='course/commonnotification')
def commonnotification(request):

    notification_courses = CourseApply.objects.all()
    notification_trainers = TrainerApply.objects.all()

    contex = {

        "notification_courses": notification_courses,
        "notification_trainers": notification_trainers

    }

    return render(request, "commonnotification.html", contex)


@login_required(login_url='course/addphoto')
def addphoto(request, id):
    form = CourseGallery(request.POST or None, request.FILES or None)

    if form.is_valid():
        course_photo = form.save(commit=False)
        course_photo.course = CourseBoss.objects.filter(id=id).first()
        course_photo.save()
        return redirect("course:detailcourse", id=id)

    contex = {
        "form": form,
    }

    return render(request, "addphoto.html", contex)


@login_required(login_url='course/blogdetails')
def blogdetails(request, id):
    blog = CoursePhoto.objects.filter(id=id).first()

    contex = {
        "blog": blog,
    }

    return render(request, "blogdetails.html", contex)


@login_required(login_url='course/addlessonplan')
def addlessonplan(request, id):
    form = CreateLessonPlan(request.POST or None)
    if form.is_valid():
        courseplan = form.save(commit=False)
        courseplan.user = request.user
        courseplan.course = CourseBoss.objects.filter(id=id).first()
        courseplan.save()
        messages.success(request, "Dərs planı əlavə edildi")
        return redirect("course:detailcourse", id=id)

    contex = {
        "form": form,
    }

    return render(request, "lessonplan.html", contex)


@login_required(login_url='course/updatelessonplan')
def updatelessonplan(request, id):
    lessonplan = get_object_or_404(LessonPlan, id=id)
    courseid = LessonPlan.objects.get(id=id).course_id
    form = CreateLessonPlan(request.POST or None, instance=lessonplan)
    if form.is_valid():
        plan = form.save(commit=False)
        plan.user = request.user
        plan.save()

        messages.success(request, "Dərs planı uğurla yeniləndi")

        return redirect("course:detailcourse", id=courseid)

    contex = {
        "form": form,

    }
    return render(request, "updatelessonplan.html", contex)


@login_required(login_url='course/deletelessonplan')
def deletelessonplan(request, id):

    lessonplan = get_object_or_404(LessonPlan, id=id)
    courseid = LessonPlan.objects.get(id=id).course_id
    lessonplan.delete()
    messages.success(request, "Dərs planı silindi")
    return redirect("course:detailcourse", id=courseid)


def detailcourse(request, id):
    course = CourseBoss.objects.filter(id=id).first()
    course_branch = Branchs.objects.filter(branch_id=id)
    course_apply = CourseApply.objects.filter(course_id=id)
    course_type = CourseType.objects.filter(id=id)
    lesson_plan = LessonPlan.objects.filter(course_id=id)
    form = AddComment()

    contex = {
        "course_values": course,
        "course_branch": course_branch,
        "course_type": course_type,
        "courseapply": course_apply,
        "lessonplans": lesson_plan,
        "form": form,
    }
    return render(request, "detailcourse.html", contex)


@login_required(login_url='course/addevent')
def addevent(request, id):
    form = CreateEvent(request.POST or None, request.FILES or None)

    if form.is_valid():
        event = form.save(commit=False)
        event.user = request.user
        event.trainer = Trainer.objects.filter(id=id).first()
        event.save()
        messages.success(request, "Event əlavə edildi")

        return redirect("course:detailtrainers", id=id)

    contex = {
        "form": form,
    }

    return render(request, "addevent.html", contex)


@login_required(login_url='course/eventdetails')
def eventdetails(request, id):
    eventdetail = Event.objects.filter(trainer=id).first()

    contex = {
        "eventdetail": eventdetail,

    }

    return render(request, "eventdetails.html", contex)


@login_required(login_url='course/eventapplynotification')
def eventapplynotification(request, id):
    eventapplyinfos = EventApply.objects.filter()

    keyword = request.GET.get("name")
    if keyword:
        eventapplyinfos = EventApply.objects.filter(user__name__icontains=keyword)
        return render(request, "eventnotification.html", {"eventapplyinfos": eventapplyinfos})

    contex = {
        "eventapplyinfos": eventapplyinfos,


    }

    return render(request, "eventnotification.html", contex)


@login_required(login_url='course/deleteevent')
def deleteevent(request, id):
    event = get_object_or_404(Event, trainer=id)
    event.delete()
    messages.success(request, "Event silindi")
    return redirect("course:detailtrainers", id=id)


@login_required(login_url='course/updateevent')
def updateevent(request, id):
    event = get_object_or_404(Event, trainer=id)
    form = CreateEvent(request.POST or None,
                       request.FILES or None, instance=event)

    if form.is_valid():
        event = form.save(commit=False)
        event.user = request.user
        event.trainer = Trainer.objects.filter(id=id).first()
        event.save()

        messages.success(request, "Event ugurla yenilendi")

        return redirect("course:detailtrainers", id=id)

    contex = {
        "form": form,

    }

    return render(request, "updateevent.html", contex)


@login_required(login_url='/user/login')
def applyevent(request, id):
    form = ApplyEventForm(request.POST or None)
    if form.is_valid():
        applyevent = form.save(commit=False)
        applyevent.user = request.user
        applyevent.trainer = Trainer.objects.get(id=id).user_id
        applyevent.event = Event.objects.filter(trainer=id).first()
        applyevent.save()
        messages.success(request, "Müraciət edildi")
        return redirect("course:detailtrainers", id=id)

    contex = {
        "form": form,

    }

    return render(request, "applyevent.html", contex)


def detailtrainers(request, id):
    trainer = Trainer.objects.filter(id=id).first()
    event = Event.objects.filter(trainer=id).first()
    contex = {
        "trainer": trainer,
        "event": event
    }
    return render(request, "detailtrainers.html", contex)


@login_required(login_url='course/updatecourse')
def updatecourse(request, id):
    course = get_object_or_404(CourseBoss, id=id)
    form = CourseInfo(request.POST or None,
                      request.FILES or None, instance=course)
    if form.is_valid():
        course = form.save(commit=False)
        course.user = request.user
        course.save()

        messages.success(request, "Kurs ugurla yenilendi")

        return redirect("course:detailcourse", id=id)

    contex = {
        "form": form,

    }

    return render(request, "updatecourse.html", contex)


@login_required(login_url='course/updatetrainer')
def updatetrainer(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    form = TrainerInfo(request.POST or None,
                       request.FILES or None, instance=trainer)

    if form.is_valid():
        trainer = form.save(commit=False)
        trainer.user = request.user
        trainer.save()

        messages.success(request, "Treyner melumatları yenilendi")

        return redirect("course:detailtrainers", id=id)

    contex = {
        "form": form,

    }

    return render(request, "updatetrainer.html", contex)


@login_required(login_url='course/applyexam')
def applyexam(request, id):
    apply_exam = ExamApply()
    exam_data = Exam()

    if request.method == "POST":
        apply_exam.student_name = request.user.name
        apply_exam.student_surname = request.user.surname
        apply_exam.student_email = request.user.email
        apply_exam.course = CourseBoss.objects.filter(id=id).first()
        apply_exam.exam = Exam.objects.get(course_id=id)
        exam_data.save()
        apply_exam.save()

        return redirect("course:courses")

    return render(request, "applyexam.html")


@login_required(login_url='course/deletecourse')
def deletecourse(request, id):
    course = get_object_or_404(CourseBoss, id=id)
    course.delete()
    messages.success(request, "Kurs silindi")
    return redirect("course:courses")


@login_required(login_url='course/deletetrainer')
def deletetrainer(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    trainer.delete()
    messages.success(request, "Təlimçi silindi")
    return redirect("course:courses")


@login_required(login_url='course/updatebranch')
def updatebranch(request, id):
    branch = get_object_or_404(Branchs, id=id)
    courseid = Branchs.objects.get(id=id).branch_id
    form = CourseBranch(request.POST or None, instance=branch)
    if form.is_valid():
        branch = form.save(commit=False)
        branch.save()
        messages.success(request, "Filial yeniləndi")

        return redirect("course:detailcourse", id=courseid)

    contex = {
        "form": form,
        "branch": branch

    }

    return render(request, "updatebranch.html", contex)


@login_required(login_url='course/deletebranch')
def deletebranch(request, id):
    branch = get_object_or_404(Branchs, id=id)
    courseid = Branchs.objects.get(id=id).branch_id
    branch.delete()
    messages.success(request, "Filial silindi")
    return redirect("course:detailcourse", id=courseid)


@login_required(login_url='course/comment')
def comment(request, id):
    course = get_object_or_404(CourseBoss, id=id)

    form = AddComment(request.POST or None)

    if form.is_valid():
        addcomment = form.save(commit=False)
        addcomment.comment_author = request.user
        addcomment.course = get_object_or_404(CourseBoss, id=id)
        addcomment.save()

        return redirect("course:detailcourse", id=id)


@login_required(login_url='course/gallery')
def gallery(request, id):
    photo = CoursePhoto.objects.filter(course_id=id)

    contex = {
        "photo_gallerys": photo,
    }

    return render(request, "photogallery.html", contex)


@login_required(login_url='course/confirm')
def confirm(request, id):
    status = CourseApply.objects.filter(id=id).first()
    courseid = CourseApply.objects.get(id=id).course_id
    status.confirm = 1
    status.pending = 0
    status.cancel = 0
    status.save()
    messages.success(request, "Müraciət təsdiqləndi")
    return redirect("course:coursenotification", id=courseid)


@login_required(login_url='course/confirmtrainer')
def confirmtrainer(request, id):
    status = TrainerApply.objects.filter(id=id).first()
    trainerid = TrainerApply.objects.get(id=id).trainer_id
    status.confirm = 1
    status.pending = 0
    status.cancel = 0
    status.save()
    messages.success(request, "Müraciət təsdiqləndi")
    return redirect("course:trainernotification", id=trainerid)


@login_required(login_url='course/canceltrainer')
def canceltrainer(request, id):
    status = TrainerApply.objects.filter(id=id).first()
    status.confirm = 0
    status.pending = 0
    status.cancel = 1
    status.save()
    messages.success(request, "Müraciətdən imtina edildi")
    return redirect("course:trainernotification", id=id)


@login_required(login_url='course/cancel')
def cancel(request, id):
    courseid = CourseApply.objects.get(id=id).course_id
    status = CourseApply.objects.filter(id=id).first()
    status.confirm = 0
    status.pending = 0
    status.cancel = 1
    status.save()
    messages.success(request, "Müraciətdən imtina edildi")
    return redirect("course:coursenotification", id=courseid)

def faq(request):
    return render (request,"faq.html")


def createblog(request):
    
    form = AddBlog(request.POST or None,
                       request.FILES or None)

    if form.is_valid():
        blog = form.save(commit=False)
        blog.user = request.user
        blog.save()

        messages.success(request, "Məqaləniz əlavə edildi")

        return redirect("course:articles")

    contex = {
        "form": form,

    }

    return render(request, "addblog.html", contex)

def articles(request):
    article = CreateBlog.objects.all()
    
    contex = {
        "articles": article,

    }
    return render (request,"articles.html", contex)

def commonarticledetails(request,id):
    
    article = CreateBlog.objects.filter(user_id=id)
    
    contex = {
        "article": article,

    }
    return render (request,"commonblogdetail.html", contex)
    
