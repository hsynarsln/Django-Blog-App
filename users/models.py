from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

# Create your models here.


#! Adding New Fields to Default User by Using AbstractUser
# * Mevcut default user'a ilave field eklemek için AbstractUser'ı kullanıyoruz. Default user'a ilave olarak iki tane field ekliyoruz.

class User(AbstractUser):

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = models.ImageField(
        upload_to='profile_pics', blank=True)
    bio = models.TextField(blank=True)
