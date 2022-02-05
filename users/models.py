from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


#! Adding New Fields to Default User by Using AbstractUser
# * Mevcut default user'a ilave field eklemek için AbstractUser'ı kullanıyoruz. Default user'a ilave olarak iki tane field ekliyoruz.


class User(AbstractUser):
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
