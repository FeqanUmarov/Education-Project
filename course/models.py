from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from tokenize import blank_re
from urllib import request
from django.db import DatabaseError, models
from user.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField




# Create your models here.
class CourseType(models.Model):
    course_type_select = models.CharField(max_length=20)

    def __str__(self):
        return self.course_type_select
    
    
class Location(models.Model):
    location_select = models.CharField(max_length=50)

    def __str__(self):
        return self.location_select



class CourseBoss(models.Model):
    is_course = models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course_name = models.CharField(max_length=30)
    course_type = models.ForeignKey(CourseType, on_delete=models.CASCADE)
    course_phone = models.CharField(max_length=200)
    course_slogan = models.CharField(max_length=50)
    course_email = models.EmailField(max_length=254)
    course_location = models.URLField(max_length=200)
    website = models.URLField(max_length=200,null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    facebook = models.URLField(max_length=200)
    #course_contact = models.CharField(max_length=100)
    course_logo = models.ImageField(null=True, blank = True)
    course_profile = models.ImageField(null=True, blank = True)

    def __str__(self):
        return '%s' % (self.course_name)
    
class Trainer(models.Model):
    is_teacher = models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    study_field = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)
    facebook = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    study_plan = RichTextField()
    note = RichTextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    
    def __str__(self):
        return '%s' % (self.study_field)
    


class Branchs(models.Model):
    branch = models.ForeignKey(CourseBoss,on_delete=models.CASCADE)
    location = models.URLField(max_length=200)
    adress = models.CharField(max_length=255)
    contact = models.CharField(max_length=30)
    def __str__(self):
        return '%s' % (self.adress)

class CoursePhoto(models.Model):
    course = models.ForeignKey(CourseBoss,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = RichTextField()
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
    course = models.ForeignKey(CourseBoss,  on_delete=models.CASCADE)
    apply_title = models.CharField(max_length=30)
    apply_content = models.CharField(max_length=100)
    apply_date = models.DateTimeField(auto_now_add=True)
    
    
class TrainerApply(models.Model):
    confirm = models.BooleanField(default=False)
    pending = models.BooleanField(default=True)
    cancel = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    apply_title = models.CharField(max_length=30)
    apply_content = models.CharField(max_length=100)
    apply_date = models.DateTimeField(auto_now_add=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    
    
class LessonPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseBoss, on_delete=models.CASCADE)
    lessonplan = RichTextField()
    
    
class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = RichTextField()
    start_date = models.DateField()
    end_date = models.DateField()
    event_day = models.DateField()
    event_location = models.URLField()
    event_adress = models.CharField(max_length=200)
    trainer = models.ForeignKey(Trainer,on_delete=models.CASCADE)
    photo = models.ImageField(max_length=30)
    

class EventApply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    trainer = models.IntegerField()
    apply_case = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)