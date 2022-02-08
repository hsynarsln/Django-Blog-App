
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(
        upload_to='post_pics', blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    POST_CATEGORY_CHOICES = [
        ('PY', 'Python'),
        ('JS', 'Javascript'),
        ('DJ', 'Django'),
        ('CSS', 'CSS'),
        ('HTML', 'HTML'),
    ]
    category = models.CharField(
        max_length=4, choices=POST_CATEGORY_CHOICES, default='DJ')
    status = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
