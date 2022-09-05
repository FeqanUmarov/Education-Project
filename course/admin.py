from django.contrib import admin
from .models import CourseBoss ,CourseType, Branchs, Comment, CourseApply, Exam, ExamApply
# Register your models here.

admin.site.register(CourseBoss)
admin.site.register(CourseType)
admin.site.register(Branchs)
admin.site.register(Comment)
admin.site.register(CourseApply)
admin.site.register(Exam)
admin.site.register(ExamApply)


