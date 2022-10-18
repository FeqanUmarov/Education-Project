

from tabnanny import verbose
from ckeditor.fields import RichTextField
from django.db import models
from user.models import User
from django.utils.translation import gettext_lazy as _


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
    is_premium = models.BooleanField(default=False)
    is_course = models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course_name = models.CharField(max_length=30, verbose_name =_("Kurs adı"))
    course_type = models.ForeignKey(CourseType, on_delete=models.CASCADE, verbose_name =_("Kursun tipi"))
    course_phone = models.CharField(max_length=200, verbose_name =_("Nömrəsi"))
    course_slogan = models.CharField(max_length=50, verbose_name =_("Slogan"))
    course_email = models.EmailField(max_length=254, verbose_name =_("Email"))
    course_location = models.URLField(max_length=200, verbose_name =_("Kursun məkanı"))
    website = models.URLField(max_length=200,null=True, blank=True, verbose_name =_("Kursun saytı"))
    twitter = models.URLField(max_length=200, null=True, blank=True, verbose_name =_("Twitter"))
    instagram = models.URLField(max_length=200, null=True, blank=True, verbose_name =_("Instagram"))
    facebook = models.URLField(max_length=200, verbose_name =_("Facebook"))
    course_logo = models.ImageField(null=True, blank = True, verbose_name =_("Kurs logosu"))
    course_profile = models.ImageField(null=True, blank = True, verbose_name =_("Kurs profil şəkili"))

    def __str__(self):
        return '%s' % (self.course_name)

class Trainer(models.Model):
    is_teacher = models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    study_field = models.CharField(max_length=100, verbose_name =_("Tədris sahəsi"))
    experience = models.CharField(max_length=50, verbose_name =_("Təcrübə"))
    facebook = models.URLField(max_length=200, verbose_name =_("Facebook"))
    instagram = models.URLField(max_length=200, null=True, blank=True, verbose_name =_("İnstagram"))
    linkedin = models.URLField(max_length=200, null=True, blank=True, verbose_name =_("Linkedin"))
    study_plan = RichTextField()
    note = RichTextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE, verbose_name =_("Ünvan"))

    def __str__(self):
        return '%s' % (self.study_field)



class Branchs(models.Model):
    branch = models.ForeignKey(CourseBoss,on_delete=models.CASCADE)
    location = models.URLField(max_length=200, verbose_name =_("Location URL"))
    adress = models.CharField(max_length=255, verbose_name =_("Ünvan"))
    contact = models.CharField(max_length=30, verbose_name =_("Əlaqə nömrəsi"))
    def __str__(self):
        return '%s' % (self.adress)

class CoursePhoto(models.Model):
    course = models.ForeignKey(CourseBoss,on_delete=models.CASCADE)
    title = models.CharField(max_length=30, verbose_name =_("Başlıq"))
    content = RichTextField()
    photo = models.ImageField(max_length=30, verbose_name =_("Şəkil"))
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
    exam_title = models.CharField(max_length=30,verbose_name =_("Imtahanın adı") )
    exam_content = models.CharField(max_length=50, verbose_name =_("İmtahan haqqında"))
    exam_date = models.DateField(verbose_name =_("imtahan tarixi"))
    branch = models.ForeignKey(Branchs,on_delete=models.CASCADE, verbose_name =_("Filial"))
    empty_space = models.CharField(max_length=10, verbose_name =_("Boş yerlər"))



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
    apply_title = models.CharField(max_length=30,verbose_name =_("Müraciət başlığı"))
    apply_content = models.CharField(max_length=100,verbose_name =_("Müraciət mövzusu"))
    apply_date = models.DateTimeField(auto_now_add=True)


class TrainerApply(models.Model):
    confirm = models.BooleanField(default=False)
    pending = models.BooleanField(default=True)
    cancel = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    apply_title = models.CharField(max_length=30,verbose_name =_("Müraciət başlığı"))
    apply_content = models.CharField(max_length=255,verbose_name =_("Müraciət mövzusu"))
    apply_date = models.DateTimeField(auto_now_add=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)



class CourseService(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseBoss, on_delete=models.CASCADE)
    service_name = models.CharField(max_length = 100)
    group_price = models.CharField(max_length = 50)
    prsonal_price = models.CharField(max_length = 50)
    about_service = RichTextField()


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name =_("Event başlığı"))
    content = RichTextField()
    start_date = models.DateField(verbose_name =_("Qeydiyyatın başlaması"))
    end_date = models.DateField(verbose_name =_("Qeydiyyatın bitməsi"))
    event_day = models.DateField(verbose_name =_("Təlimin başlaması"))
    event_location = models.URLField(verbose_name =_("Ünvan URL"))
    event_adress = models.CharField(max_length=200, verbose_name =_("Adres"))
    trainer = models.ForeignKey(Trainer,on_delete=models.CASCADE)
    photo = models.ImageField(max_length=30)


class EventApply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    trainer = models.IntegerField()
    apply_case = models.CharField(max_length=200, verbose_name =_("Müraciət səbəbi"))
    date = models.DateTimeField(auto_now_add=True)
    
    
class CreateBlog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=200,verbose_name =_("Məqalə başlığı"))
    blog_content = RichTextField(verbose_name =_("Məqalə Mövzusu"))
    photo = models.ImageField(max_length=50, verbose_name =_("Şəkil"))
    
    
    
class CourseAnswer(models.Model):
    course = models.ForeignKey(CourseBoss, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    answer = models.TextField()
    
    
class UserAnswer(models.Model):
    answercourse = models.ForeignKey(CourseAnswer, on_delete = models.CASCADE)
    course = models.ForeignKey(CourseBoss, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    answer = models.TextField()

