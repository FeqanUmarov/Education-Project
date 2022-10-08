from django.urls import path

from course import views

app_name = "course"

urlpatterns = [
    path('courses', views.courses, name="courses"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('addcourse', views.addcourse, name="addcourse"),
    path('addtrainer', views.addtrainer, name="addtrainer"),
    path('addbranch/<int:id>', views.addbranch, name="addbranch"),
    path('detailcourse/<int:id>', views.detailcourse, name="detailcourse"),
    path('detailtrainers/<int:id>', views.detailtrainers, name="detailtrainers"),
    path('updatecourse/<int:id>', views.updatecourse, name="updatecourse"),
    path('updatetrainer/<int:id>', views.updatetrainer, name="updatetrainer"),
    path('deletecourse/<int:id>', views.deletecourse, name="deletecourse"),
    path('updatebranch/<int:id>', views.updatebranch, name="updatebranch"),
    path('deletebranch/<int:id>', views.deletebranch, name="deletebranch"),
    path('comment/<int:id>', views.comment, name="comment"),
    path('addphoto/<int:id>', views.addphoto, name="addphoto"),
    path('blogdetails/<int:id>', views.blogdetails, name="blogdetails"),
    path('gallery/<int:id>', views.gallery, name="gallery"),
    path('addexam/<int:id>', views.addexam, name="addexam"),
    path('courseexam/<int:id>', views.courseexam, name="courseexam"),
    path('courseapply/<int:id>', views.courseapply, name="courseapply"),
    path('applytrainer/<int:id>', views.applytrainer, name="applytrainer"),
    path('addlessonplan/<int:id>', views.addlessonplan, name="addlessonplan"),
    path('updatelessonplan/<int:id>',
         views.updatelessonplan, name="updatelessonplan"),
    path('deletelessonplan/<int:id>',
         views.deletelessonplan, name="deletelessonplan"),
    path('coursenotification/<int:id>',
         views.coursenotification, name="coursenotification"),
    path('courseapplynotification/<int:id>',
         views.courseapplynotification, name="courseapplynotification"),
    path('commonnotification/', views.commonnotification,
         name="commonnotification"),
    path('trainernotification/<int:id>',
         views.trainernotification, name="trainernotification"),
    path('trainerapplynotification/<int:id>',
         views.trainerapplynotification, name="trainerapplynotification"),
    path('confirm/<int:id>', views.confirm, name="confirm"),
    path('confirmtrainer/<int:id>', views.confirmtrainer, name="confirmtrainer"),
    path('canceltrainer/<int:id>', views.canceltrainer, name="canceltrainer"),
    path('cancel/<int:id>', views.cancel, name="cancel"),
    path('tests', views.tests, name="tests"),
    path('applyexam/<int:id>', views.applyexam, name="applyexam"),
    path('addevent/<int:id>', views.addevent, name="addevent"),
    path('eventdetails/<int:id>', views.eventdetails, name="eventdetails"),
    path('deleteevent/<int:id>', views.deleteevent, name="deleteevent"),
    path('deletetrainer/<int:id>', views.deletetrainer, name="deletetrainer"),
    path('updateevent/<int:id>', views.updateevent, name="updateevent"),
    path('applyevent/<int:id>', views.applyevent, name="applyevent"),
    path('faq', views.faq, name="faq"),
    path('eventapplynotification/<int:id>',
         views.eventapplynotification, name="eventapplynotification"),

]
