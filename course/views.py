from email import message
from email.policy import default
from pyexpat.errors import messages
from re import I
from tkinter.messagebox import NO
from urllib import request, response
import datetime
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from course.models import CourseBoss, Branchs, CourseType,Comment,CoursePhoto, CourseApply, Exam, ExamApply, CourseService, Trainer, TrainerApply, Event, EventApply,CreateBlog,Messages
from user.models import User
from .forms import CourseInfo, CourseBranch, AddComment, CourseGallery, CourseExam, AskCourse, CreateService, TrainerInfo, AskTrainer, CreateEvent, ApplyEventForm, ApplyEventForm,AddBlog,ChatMessages
from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.core.mail import EmailMessage
# Create your views here.


def courses(request):



    keyword = request.GET.get("keyword")
    if keyword:
        courses = CourseBoss.objects.filter(course_name__contains = keyword)

        return render(request,"courses.html",{"course_values":courses})

    value = CourseBoss.objects.all()
    trainer_value = Trainer.objects.all()




    contex = {
        "course_values":value,
        "trainer_values":trainer_value,
    }

    return render(request,"courses.html",contex)




def premuimcourse(request,id):
    course = get_object_or_404(CourseBoss,id=id)
    if request.method == "POST":
        print(id)
        print("Method post" )
        course.is_premium = True
        return redirect ("course:courses")

    return render(request,"premiumcourse.html")




def aboutus(request):
    return render(request,"aboutus.html")


@login_required(login_url='course/addcourse')
def addcourse(request):
    form = CourseInfo(request.POST or None,request.FILES or None)
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

@login_required(login_url='course/addtrainer')
def addtrainer(request):
    form = TrainerInfo(request.POST or None,request.FILES or None)
    if form.is_valid():
        trainer = form.save(commit=False)
        trainer.user= request.user
        form.save()
        messages.success(request,"Treyner kimi qeydiyyatdan keçdiniz")

        return redirect ("course:courses")


    contex = {
        "form": form,
    }

    return render(request,"addtrainer.html", contex)


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
    
    if request.user.id == CourseBoss.objects.get(id=id).user_id:
        return render(request,"addexam.html", contex)
    else:
        return redirect("course:detailcourse",id=id)
    

@login_required(login_url='course/courseexam')
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
        apply.user = request.user
        apply.course = CourseBoss.objects.filter(id=id).first()
        apply.save()

        return redirect("course:detailcourse",id=id)


    contex = {
        "form": form,
    }

    return render(request,"courseapply.html", contex)

@login_required(login_url='course/applytrainer')
def applytrainer(request,id):
    form = AskTrainer(request.POST or None)

    if form.is_valid():
        trainer_apply = form.save(commit=False)
        trainer_apply.user = request.user
        trainer_apply.trainer = Trainer.objects.filter(id=id).first()
        userid=Trainer.objects.get(id=id).user_id
        email = User.objects.get(id=userid).email

        trainer_apply.save()
        email = EmailMessage(
        'Müraciət',
        'Yeni bir tələbə müraciət etdi',
        settings.EMAIL_HOST_USER,
        [str(email)]
        )
        email.fail_silently = False
        email.send()



        return redirect("course:detailtrainers",id=id)

    contex = {
        "form": form,
    }


    return render(request, "applytrainer.html", contex)

@login_required(login_url='course/trainernotification')
def trainernotification(request,id):
    student_apply = TrainerApply.objects.filter(trainer=id)

    contex = {
        "student_applys":student_apply,
    }
    
    if request.user.id == Trainer.objects.get(id=id).user_id:
        return render(request, "trainernotification.html", contex)
    else:
        return redirect("course:detailtrainers",id=id)


@login_required(login_url='course/trainerapplynotification')
def trainerapplynotification(request,id):
    student_infos = TrainerApply.objects.filter(trainer=id)

    contex = {
        "student_infos":student_infos

    }


    return render(request, "trainerapplynotification.html", contex)





@login_required(login_url='course/coursenotification')
def coursenotification(request,id):

    student_info = CourseApply.objects.filter(course_id=id)

    contex = {
        "student_infos": student_info,
    }

    if request.user.id == CourseBoss.objects.get(id=id).user_id:
        return render(request,"coursenotification.html",contex)
    else:
        return redirect("course:detailcourse",id=id)


@login_required(login_url='course/courseapplynotification')
def courseapplynotification(request,id):

    student_info = CourseApply.objects.filter(course_id=id)

    contex = {
        "student_infos": student_info,

    }
    
    

    return render(request,"courseapplynotification.html",contex)






@login_required(login_url='course/commonnotification')
def commonnotification(request):


    notification_courses = CourseApply.objects.all()
    notification_trainers = TrainerApply.objects.all()


    contex = {

        "notification_courses":notification_courses,
        "notification_trainers":notification_trainers

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

    if request.user.id == CourseBoss.objects.get(id=id).user_id:
        return render(request,"addphoto.html", contex)
    else:
        return redirect("course:detailcourse",id=id)
    
    

@login_required(login_url='course/blogdetails')
def blogdetails(request, id):
    blog = CoursePhoto.objects.filter(id=id).first()

    contex = {
        "blog": blog,
    }

    return render (request, "blogdetails.html",contex)



@login_required(login_url='course/addservice')
def addservice(request, id):
    form = CreateService(request.POST or None)
    if form.is_valid():
        course_service = form.save(commit=False)
        course_service.user = request.user
        course_service.course = CourseBoss.objects.filter(id=id).first()
        course_service.save()
        return redirect("course:detailcourse",id=id)

    contex = {
        "form":form,
    }
    
    
    if request.user.id == CourseBoss.objects.get(id=id).user_id:
        return render (request, "service.html", contex)
    else:
        return redirect("course:detailcourse",id=id)

@login_required(login_url='course/updateservice')
def updateservice(request, id):
    course_service = get_object_or_404(CourseService,id=id)
    courseid = CourseService.objects.get(id=id).course_id
    form = CreateService(request.POST or None, instance=course_service)
    if form.is_valid():
        plan = form.save(commit=False)
        plan.user = request.user
        plan.save()

        messages.success(request,"Dərs planı uğurla yeniləndi")

        return redirect ("course:detailcourse", id=courseid)

    contex = {
        "form":form,

    }
    if request.user.id == CourseService.objects.get(id=id).user_id:
        return render(request, "updatelessonplan.html",contex)
    else:
        return redirect("course:detailcourse",id=id)


def detailservice(request,id):
    service = CourseService.objects.filter(id=id).first()

    contex = {
        "service":service,

    }
    return render(request, "detailsservice.html",contex)




@login_required(login_url='course/deleteservice')
def deleteservice(request,id):

    lessonplan = get_object_or_404(CourseService,id=id)
    courseid=CourseService.objects.get(id=id).course_id
    if request.user.id == CourseService.objects.get(id=id).user_id:
        lessonplan.delete()
        return redirect ("course:detailcourse", id=courseid)
    else:
        return redirect("course:detailcourse",id=id)



def detailcourse(request,id):
    course = CourseBoss.objects.filter(id=id).first()
    course_branch = Branchs.objects.filter(branch_id=id)
    course_apply = CourseApply.objects.filter(course_id = id)
    course_type = CourseType.objects.filter(id=id)
    services = CourseService.objects.filter(course_id=id)
    form = AddComment()

    contex = {
        "course_values":course,
        "course_branch":course_branch,
        "course_type":course_type,
        "courseapply":course_apply,
        "services":services,
        "form":form,
    }
    return render(request, "detailcourse.html",contex)


@login_required(login_url='course/addevent')
def addevent(request,id):
    form = CreateEvent(request.POST or None, request.FILES or None)

    if form.is_valid():
        event = form.save(commit=False)
        event.user = request.user
        event.trainer = Trainer.objects.filter(id=id).first()
        event.save()

        return redirect("course:detailtrainers",id=id)


    contex ={
        "form":form,
    }
    
    if request.user.id == Trainer.objects.get(id=id).user_id:
        return render (request, "addevent.html", contex)
    else:
        return redirect("course:detailtrainers",id=id)

@login_required(login_url='course/eventdetails')
def eventdetails(request,id):
    eventdetail = Event.objects.filter(trainer=id).first()

    contex = {
        "eventdetail":eventdetail,

    }

    return render(request, "eventdetails.html", contex)







@login_required(login_url='course/eventapplynotification')
def eventapplynotification(request,id):
    eventapplyinfos = EventApply.objects.filter()

    keyword = request.GET.get("name")
    if keyword:
        eventapplyinfos = User.objects.filter(name__contains = keyword)
        return render(request,"eventnotification.html",{"eventapplyinfos":eventapplyinfos})




    contex = {
        "eventapplyinfos":eventapplyinfos,


    }

    return render(request, "eventnotification.html", contex)









@login_required(login_url='course/deleteevent')
def deleteevent(request,id):
    event = get_object_or_404(Event,trainer=id)
    if request.user.id == Trainer.objects.get(id=id).user_id:
        event.delete()
        return redirect("course:detailtrainers",id=id)
    else:
        return redirect("course:detailtrainers",id=id)
        



@login_required(login_url='course/updateevent')
def updateevent(request,id):
    event = get_object_or_404(Event,trainer=id)
    form = CreateEvent(request.POST or None, request.FILES or None , instance=event)

    if form.is_valid():
        event = form.save(commit=False)
        event.user = request.user
        event.trainer = Trainer.objects.filter(id=id).first()
        event.save()

        messages.success(request,"Event ugurla yenilendi")

        return redirect ("course:detailtrainers",id=id)

    contex = {
        "form":form,

    }
    if request.user.id == Trainer.objects.get(id=id).user_id:
        return render(request, "updateevent.html",contex)
    else:
        return redirect ("course:detailtrainers",id=id)
        



@login_required(login_url='/user/login')
def applyevent(request,id):
    form = ApplyEventForm(request.POST or None)
    if form.is_valid():
        applyevent = form.save(commit=False)
        applyevent.user = request.user
        applyevent.trainer = Trainer.objects.get(id=id).user_id
        applyevent.event = Event.objects.filter(trainer=id).first()
        applyevent.save()
        return redirect ("course:detailtrainers",id=id)

    contex = {
        "form":form,

    }

    return render(request, "applyevent.html",contex)






def detailtrainers(request,id):
    trainer = Trainer.objects.filter(id=id).first()
    event = Event.objects.filter(trainer=id).first()
    contex = {
        "trainer":trainer,
        "event":event
        }
    return render(request,"detailtrainers.html", contex)


@login_required(login_url='course/updatecourse')
def updatecourse(request,id):
    course = get_object_or_404(CourseBoss,id=id)
    form = CourseInfo(request.POST or None, request.FILES or None , instance=course)
    if form.is_valid():
        course = form.save(commit=False)
        course.user = request.user
        course.save()

        messages.success(request,"Kurs ugurla yenilendi")

        return redirect ("course:detailcourse",id=id)

    contex = {
        "form":form,

    }
    
    if request.user.id == CourseBoss.objects.get(id=id).user_id:
        return render(request, "updatecourse.html",contex)
    else:
        return redirect("course:detailcourse",id=id)
        



@login_required(login_url='course/updatetrainer')
def updatetrainer(request,id):
    trainer = get_object_or_404(Trainer,id=id)
    form = TrainerInfo(request.POST or None, request.FILES or None , instance=trainer)

    if form.is_valid():
        trainer = form.save(commit=False)
        trainer.user = request.user
        trainer.save()

        messages.success(request,"Treyner melumatları yenilendi")

        return redirect ("course:detailtrainers",id=id)

    contex = {
        "form":form,

    }

    if request.user.id == Trainer.objects.get(id=id).user_id:
        return render(request, "updatetrainer.html",contex)
    else:
        return redirect("course:detailtrainers",id=id)
        


@login_required(login_url='course/applyexam')
def applyexam(request,id):
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

        return redirect ("course:courses")




    return render(request,"applyexam.html")








@login_required(login_url='course/deletecourse')
def deletecourse(request,id):
    course = get_object_or_404(CourseBoss,id=id)
    if request.user.id == CourseBoss.objects.get(id=id).user_id:
        course.delete()
        return redirect("course:courses")
    else:
        return redirect("course:detailcourse",id=id)
        



@login_required(login_url='course/deletetrainer')
def deletetrainer(request, id):
    trainer = get_object_or_404(Trainer,id=id)
    if request.user.id == Trainer.objects.get(id=id).user_id:
        trainer.delete()
        return redirect("course:courses")
    else:
        return redirect("course:detailtrainers",id=id)
        



@login_required(login_url='course/updatebranch')
def updatebranch(request,id):
    branch = get_object_or_404(Branchs,id=id)
    courseid = Branchs.objects.get(id=id).branch_id
    form = CourseBranch(request.POST or None, instance=branch)
    if form.is_valid():
        branch = form.save(commit=False)
        branch.save()

        return redirect("course:detailcourse", id=courseid)


    contex = {
        "form":form,
        "branch":branch

    }
   
    if request.user.id == CourseBoss.objects.get(id=courseid).user_id:
        return render(request, "updatebranch.html",contex)
    else:
        return redirect("course:detailcourse", id=courseid)
        
        


@login_required(login_url='course/deletebranch')
def deletebranch(request, id):
    branch = get_object_or_404(Branchs,id=id)
    courseid = Branchs.objects.get(id=id).branch_id
    if request.user.id == CourseBoss.objects.get(id=courseid).user_id:
        branch.delete()
        return redirect("course:detailcourse", id=courseid)
    else:
        return redirect("course:detailcourse", id=courseid)
        


@login_required(login_url='course/comment')
def comment(request,id):
    course = get_object_or_404(CourseBoss,id=id)

    form = AddComment(request.POST or None)

    if form.is_valid():
        addcomment = form.save(commit=False)
        addcomment.comment_author = request.user
        addcomment.course = get_object_or_404(CourseBoss,id=id)
        addcomment.save()

        return redirect("course:detailcourse",id=id)


@login_required(login_url='course/gallery')
def gallery(request,id):
    photo = CoursePhoto.objects.filter(course_id=id)

    contex = {
        "photo_gallerys":photo,
    }

    return render (request,"photogallery.html",contex)


@login_required(login_url='course/confirm')
def confirm(request, id):
    status = CourseApply.objects.filter(id=id).first()
    courseid = CourseApply.objects.get(id=id).course_id
    if request.user.id == CourseBoss.objects.get(id=courseid).user_id:
        status.confirm = 1
        status.pending = 0
        status.cancel = 0
        status.save()
        return redirect("course:coursenotification",id=courseid)
    else:
        return redirect("course:detailcourse",id=id)
        


@login_required(login_url='course/confirmtrainer')
def confirmtrainer(request, id):
    status = TrainerApply.objects.filter(id=id).first()
    trainerid = TrainerApply.objects.get(id=id).trainer_id
    if request.user.id == Trainer.objects.get(id=trainerid).user_id:
        status.confirm = 1
        status.pending = 0
        status.cancel = 0
        status.save()
        return redirect("course:trainernotification",id=trainerid)
    else:
        return redirect("course:detailtrainers",id=trainerid)


@login_required(login_url='course/canceltrainer')
def canceltrainer(request, id):
    status = TrainerApply.objects.filter(id=id).first()
    trainerid = TrainerApply.objects.get(id=id).trainer_id
    if request.user.id == Trainer.objects.get(id=trainerid).user_id:
        status.confirm = 0
        status.pending = 0
        status.cancel = 1
        status.save()
        return redirect("course:trainernotification",id=id)
    else:
        return redirect("course:detailtrainers",id=trainerid)
        


@login_required(login_url='course/cancel')
def cancel(request,id):
    courseid = CourseApply.objects.get(id=id).course_id
    status = CourseApply.objects.filter(id=id).first()
    if request.user.id == CourseApply.objects.get(id=courseid).user_id:
        status.confirm = 0
        status.pending = 0
        status.cancel = 1
        status.save()
        return redirect("course:coursenotification",id=courseid)
    else:
        return redirect("course:detailcourse",id=courseid)
        


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

    article = CreateBlog.objects.filter(user_id=id).first()

    contex = {
        "article": article,

    }
    return render (request,"commonblogdetail.html", contex)

def updatearticle(request,id):
    blog = get_object_or_404(CreateBlog,user_id=id)
    form = AddBlog(request.POST or None, request.FILES or None , instance=blog)

    contex = {
        "form": form,

    }
    
    if request.user.id == get_object_or_404(CreateBlog,user_id=id):
        return render (request,"updatearticle.html", contex)
    else:
        return redirect("course:articles")

def deletearticle(request,id):
    blog = get_object_or_404(CreateBlog,user_id=id)
    if request.user.id == get_object_or_404(CreateBlog,user_id=id):
        blog.delete()
        return redirect("course:articles")
    else:
        return redirect("course:articles")



# def courseanswer(request,id):
#     form = AnswerCourse(request.POST or None)

#     if form.is_valid():
#         answer = form.save(commit=False)
#         answer.course = CourseApply.objects.get(id=id).course
#         answer.user = CourseApply.objects.get(id=id).user
#         answer.save()
#         return redirect("course:courses")



#     contex = {
#         "form": form,

#     }
#     return render (request,"courseanswer.html", contex)


def coursemessage(request,id):
    courseid = CourseApply.objects.get(id=id).course
    user_id = CourseApply.objects.get(id=id).user

    messages_ = Messages.objects.filter(user=user_id)
    form = ChatMessages(request.POST or None)
    if form.is_valid():
        answer = form.save(commit=False)
        answer.course = courseid
        answer.user = user_id
        answer.course_message = True
        answer.save()



    contex = {
        "courseid":courseid,
        "messages_chats": messages_,
        "form":form

    }
    course_id = CourseApply.objects.get(id=id).course_id
    if request.user.id == CourseBoss.objects.get(id=course_id).user_id:
        return render (request,"messages.html", contex)
    else:
        return redirect("course:detailcourse", id=course_id)


def usermessage(request,id):
    courseid = CourseApply.objects.get(id=id).course
    user_id = CourseApply.objects.get(id=id).user

    messages_ = Messages.objects.filter(user=user_id)
    form = ChatMessages(request.POST or None)
    if form.is_valid():
        answer = form.save(commit=False)
        answer.course = courseid
        answer.user = user_id
        answer.course_message = False
        answer.save()



    contex = {
        "courseid":courseid,
        "messages_chats": messages_,
        "form":form

    }
    userid = CourseApply.objects.get(id=id).user_id
    course_id = CourseApply.objects.get(id=id).course_id
    if request.user.id == userid:
        return render (request,"messages.html", contex)
    else:
        return redirect("course:detailcourse", id=course_id)


























