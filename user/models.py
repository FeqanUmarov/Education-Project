from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=30, verbose_name=_("Full name"))
    surname = models.CharField(max_length=30, verbose_name="Surname")
    username = models.CharField(max_length=50, unique=True , verbose_name="Username")
    email = models.EmailField(max_length=254 , verbose_name="Email")
    user_profile = models.ImageField(null=True, blank = True, verbose_name="Profil picture")
    phone = models.CharField(max_length=50,verbose_name="Phone number")



        



