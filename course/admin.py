from django.contrib import admin
from .models import CourseBoss ,CourseType, Branchs, Comment, CourseApply, Exam, ExamApply,LessonPlan, Trainer, TrainerApply, Event, EventApply, Location, CoursePhoto, CreateBlog
# Register your models here.

admin.site.register(CourseBoss)
admin.site.register(CourseType)
admin.site.register(Branchs)
admin.site.register(Comment)
admin.site.register(CourseApply)
admin.site.register(Exam)
admin.site.register(ExamApply)
admin.site.register(LessonPlan)
admin.site.register(Trainer)
admin.site.register(TrainerApply)
admin.site.register(Event)
admin.site.register(EventApply)
admin.site.register(Location)
admin.site.register(CoursePhoto)
admin.site.register(CreateBlog)


