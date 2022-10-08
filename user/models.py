from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=30, verbose_name=_("Adı"))
    surname = models.CharField(max_length=30, verbose_name=_("Soyad"))
    username = models.CharField(
        max_length=50, unique=True, verbose_name=_("Istifadəçi adı"))
    email = models.EmailField(
        max_length=254, verbose_name=_("Email"), unique=True)
    user_profile = models.ImageField(
        null=True, blank=True, verbose_name=_("User şəkili"))
    phone = models.CharField(max_length=50, verbose_name=_("Telefon"))
    
    def save(self, *args, **kwargs) -> None:
        self.email.lower()
        return super(User, self).save(*args, **kwargs)
