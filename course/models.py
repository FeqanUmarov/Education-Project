from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from tokenize import blank_re
from urllib import request
from django.db import DatabaseError, models
from user.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import datetime




# Create your models here.
class CourseType(models.Model):
    course_type_select = models.CharField(max_length=20)

    def __str__(self):
        return self.course_type_select



class CourseBoss(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    #name = models.CharField(max_length=20)
    #surname = models.CharField(max_length=20)
    course_name = models.CharField(max_length=30)
    course_type = models.ForeignKey(CourseType, on_delete=models.CASCADE)
    course_slogan = models.CharField(max_length=50)
    #course_email = models.EmailField(max_length=254)
    course_location = models.CharField(max_length=100)
   #course_contact = models.CharField(max_length=100)
    course_logo = models.ImageField(null=True, blank = True)
    course_profile = models.ImageField(null=True, blank = True)

    def __str__(self):
        return '%s' % (self.course_name)


class Branchs(models.Model):
    branch = models.ForeignKey(CourseBoss,on_delete=models.CASCADE)
    location = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    def __str__(self):
        return '%s' % (self.adress)

class CoursePhoto(models.Model):
    course = models.ForeignKey(CourseBoss,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=50)
    branch = models.ForeignKey(Branchs,on_delete=models.CASCADE)
    photo = models.ImageField(max_length=30)
    def __str__(self):
        return '%s' % (self.title)


class Comment(models.Model):
    course = models.ForeignKey(CourseBoss,on_delete=models.CASCADE,verbose_name="Kurs", related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="Ad")
    comment_content = models.CharField(max_length=200,verbose_name="Rəy")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' %(self.comment_content)

class Exam(models.Model):
    course = models.ForeignKey(CourseBoss,on_delete=models.CASCADE)
    exam_title = models.CharField(max_length=30)
    exam_content = models.CharField(max_length=50)
    exam_date = models.DateField()
    branch = models.ForeignKey(Branchs,on_delete=models.CASCADE)
    empty_space = models.CharField(max_length=10)



class ExamApply(models.Model):
    student_name = models.CharField(max_length=20)
    student_surname = models.CharField(max_length=20)
    student_email = models.CharField(max_length=254)
    course = models.ForeignKey(CourseBoss,on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)


class CourseApply(models.Model):
    confirm = models.BooleanField(default=False)
    pending = models.BooleanField(default=True)
    cancel = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_student = models.IntegerField()
    course = models.ForeignKey(CourseBoss,  on_delete=models.CASCADE)
    student_name = models.CharField(max_length=30)
    student_surname = models.CharField(max_length=30)
    apply_title = models.CharField(max_length=30)
    apply_content = models.CharField(max_length=100)
    apply_date = models.DateTimeField(auto_now_add=True)
    student_email = models.CharField(max_length=50)
    student_phone = models.CharField(max_length=50)