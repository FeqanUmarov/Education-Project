from os import stat
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from course import views

app_name = "course"

urlpatterns = [
    path('courses', views.courses, name = "courses"),
    path('addcourse', views.addcourse, name = "addcourse"),
    path('addbranch/<int:id>', views.addbranch, name = "addbranch"),
    path('detailcourse/<int:id>', views.detailcourse, name = "detailcourse"),
    path('updatecourse/<int:id>', views.updatecourse, name = "updatecourse"),
    path('deletecourse/<int:id>', views.deletecourse, name = "deletecourse"),
    path('updatebranch/<int:id>', views.updatebranch, name = "updatebranch"),
    path('comment/<int:id>', views.comment, name = "comment"),
    path('addphoto/<int:id>', views.addphoto, name = "addphoto"),
    path('gallery/<int:id>', views.gallery, name = "gallery"),
    path('addexam/<int:id>', views.addexam, name = "addexam"),
    path('courseexam/<int:id>', views.courseexam, name = "courseexam"),
    path('courseapply/<int:id>', views.courseapply, name = "courseapply"),
    path('coursenotification/<int:id>', views.coursenotification, name = "coursenotification"),
    path('commonnotification/', views.commonnotification, name = "commonnotification"),
    path('confirm/<int:id>', views.confirm, name = "confirm"),
    path('cancel/<int:id>', views.cancel, name = "cancel"),
    path('delete/<int:id>', views.delete, name = "delete"),
    path('tests', views.tests, name = "tests"),
    path('applyexam/<int:id>',views.applyexam, name="applyexam"),
]
