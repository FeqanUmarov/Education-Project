from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    is_course = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    name = models.CharField(max_length=30, verbose_name="Adınız")
    surname = models.CharField(max_length=30, verbose_name="Soyadınız")
    username = models.CharField(max_length=50, unique=True , verbose_name="İstifadəçi adınız")
    email = models.EmailField(max_length=254 , verbose_name="Emailiniz")
    user_profile = models.ImageField(null=True, blank = True)


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=50)
    course_email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.course_name)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    university = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.university)
    
    
class Tutor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    study_field = models.CharField(max_length=30)
    experience = models.CharField(max_length=20)
    teacher_number = models.CharField(max_length=100)
        



