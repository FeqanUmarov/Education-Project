from django.db import models

# Create your models here.
class UserQuery(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    course_name = models.CharField(max_length=30)
    course_email = models.EmailField(max_length=254)

    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.name, self.surname,self.email,self.phone, self.username,self.course_name, self.course_email)


class TutorQuery(models.Model):
    teachername = models.CharField(max_length=20)
    teachersurname = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    teacherphone = models.CharField(max_length=100)
    experience = models.CharField(max_length=10)
    study_field = models.CharField(max_length=30)