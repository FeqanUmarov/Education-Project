# Create your models here.
from django.db import models

from course import models as course_models
from user.models import User
from utils.models import TrackingModel

# Create your models here.


class Exam(TrackingModel):
    """
    Bu model trainer ve ya kurs terefinden yaradilacag imthian modeli olacag
    kurs terefinden yaradilirsa kursun id-sini al foregin key hissesine yaz 
    trainer terefinden yaradilirsa tarinerin id-sini trainer field-ine yaz
    """
    class DurationType(models.IntegerChoices):
        MINUTE = 1, "dəqiqə"
        HOUR = 2, "Saat"

    title = models.CharField("başlıq", max_length=75)
    course = models.ForeignKey(course_models.CourseBoss, related_name='exams',
                               on_delete=models.CASCADE, null=True, blank=True)
    triner = models.ForeignKey(course_models.Trainer, related_name='exams',
                               on_delete=models.CASCADE, null=True, blank=True)
    duration_type = models.PositiveIntegerField(choices=DurationType.choices)
    duration = models.PositiveIntegerField("imtihan müddəti")
    closing_date = models.DateTimeField("bitmə vaxtı")
    retake_count = models.PositiveIntegerField(
        "limit yoxdursa boş buraxın", null=True, blank=True)

    def __str__(self) -> str:
        return self.course if self.course else self.trainer


class Question(TrackingModel):
    """
    Bu model da her yaradilan sual ucundu ve hansi imtihana bagli oldugunu 
    mueyyen elemek ucun exam model-ine baglanir 
    """
    question = models.TextField()
    exam = models.ForeignKey(
        Exam, related_name='questions', on_delete=models.CASCADE)
    rank = models.PositiveIntegerField("sıra nömrəsi", null=True, blank=True)

    class Meta:
        ordering = ["-rank", "created_at"]

    def __str__(self) -> str:
        return self.question[:20]


class Answer(TrackingModel):
    """
    Bu da cavablar modelidi hansi sual ucun cavablar yaradilirsa burda qyed eliyirik
    """
    answer = models.TextField("answer")
    question = models.ForeignKey(
        Question, related_name='answers', on_delete=models.CASCADE, null=True, blank=True)
    is_valid_answer = models.BooleanField("doğru cavabdır", default=False)

    def __str__(self) -> str:
        return self.answer[:20]


class UserExam(TrackingModel):

    exam = models.ForeignKey(
        Exam, related_name='exammers', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='exams',
                             on_delete=models.CASCADE)
    finished_at = models.DateTimeField()

    @property
    def started_at(self):
        return self.created_at

    @property
    def exam_duration(self):
        return self.finished_at - self.created_at

    def __str__(self) -> str:
        return self.exam.title


class UserAnswer(TrackingModel):
    answer = models.ForeignKey(
        Answer, related_name='user_answers', on_delete=models.CASCADE)
    user_exam = models.ForeignKey(
        UserExam, related_name='answers', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user} - {self.answer}"