from django.contrib import admin
from .models import CourseBoss ,CourseType, Branchs, Comment, CourseApply, Exam, ExamApply,CourseService, Trainer, TrainerApply, Event, EventApply, Location, CoursePhoto
# Register your models here.

admin.site.register(CourseBoss)
admin.site.register(CourseType)
admin.site.register(Branchs)
admin.site.register(Comment)
admin.site.register(CourseApply)
admin.site.register(Exam)
admin.site.register(ExamApply)
admin.site.register(CourseService)
admin.site.register(Trainer)
admin.site.register(TrainerApply)
admin.site.register(Event)
admin.site.register(EventApply)
admin.site.register(Location)
admin.site.register(CoursePhoto)


