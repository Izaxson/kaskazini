from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='img/uploads', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    body = RichTextField(blank=True, null= True)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class About(models.Model):
    about_blog = models.TextField(blank=True, null=True)


class Contact(models.Model):

    name = models.CharField(max_length=345)
    email = models.EmailField(max_length=345)
    message = models.CharField(max_length=345)
    created = models.DateTimeField(auto_now_add=True)
 
# def __str__(self):
#          return f'Message from {self.name}'

    def __str__(self):
        return self.name

class Comment(models.Model):

    name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    created = models.DateTimeField(auto_now_add=True)

# def __str__(self):
#          return f'Comment from {self.name}'
    def __str__(self):
        return self.name
