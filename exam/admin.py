from django.contrib import admin
from .models import Exam,Question,Answer,UserExam,UserAnswer
# Register your models here.
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserExam)
admin.site.register(UserAnswer)
