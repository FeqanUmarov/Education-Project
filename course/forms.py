# from msilib.schema import Class
from dataclasses import fields
from multiprocessing.sharedctypes import Value
from pyexpat import model
from urllib import request

import user
from .models import CourseBoss
from django.forms import ModelForm
from django import forms

from course.models import CourseBoss, Branchs,Comment, CoursePhoto, Exam, CourseApply, ExamApply, CourseService, Trainer, TrainerApply, Event, EventApply,CreateBlog,Messages
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, EmailInput
from user.models import User
import datetime




class CourseInfo(forms.ModelForm):

    # course_name = forms.ModelChoiceField(queryset=Course.objects.all())
    class Meta:
        model = CourseBoss
        fields = ["course_name","course_type","course_phone","course_slogan","course_email","course_location","website","twitter","instagram","facebook","course_logo","course_profile"]

        widgets = {
            'course_name': forms.TextInput(attrs={'class': 'new-course'}),
        }


class CreateService(forms.ModelForm):
    class Meta:
        model = CourseService
        fields  =["service_name","group_price","prsonal_price","about_service"]


class TrainerInfo(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ["study_field","experience","facebook","instagram","linkedin","study_plan","note","location"]

class CourseBranch(forms.ModelForm):
    class Meta:
        model = Branchs
        fields = ["location","adress","contact"]
        def __init__(self, *args,**kwargs):
            super(CourseBranch, self).__init__(*args,**kwargs)
            self.fields['location'].label = "Yerlesdiyi yer"

class CourseGallery(forms.ModelForm):

    class Meta:
        model = CoursePhoto
        fields = ["title","content","photo"]




class CourseExam(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ["exam_title","exam_content","exam_date","branch","empty_space"]

class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_content"]

        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['comment_content'].widget.attrs.update({'class': 'form-control'})


class AskCourse(forms.ModelForm):
    class Meta:
        model = CourseApply
        fields = ["apply_title","apply_content"]


class AskTrainer(forms.ModelForm):
    class Meta:
        model = TrainerApply
        fields = ["apply_title","apply_content"]



class CreateEvent(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title","content","photo","start_date","end_date","event_day","event_location","event_adress"]


class ApplyEventForm(forms.ModelForm):
    class Meta:
        model = EventApply
        fields = ["apply_case"]


class AddBlog(forms.ModelForm):
    class Meta:
        model = CreateBlog
        fields = ["blog_title","blog_content","photo"]



class ChatMessages(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ["message"]

        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control'}),

        }



















