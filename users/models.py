from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.text import slugify
# Create your models here.

class Student(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12,unique=True)
    profile_pic = models.ImageField(upload_to='profile_images')
    bio = models.TextField(blank=True)
    slug = models.SlugField(unique=True,blank=True)

    def get_absolute_url(self):
        return reverse('user:student_profile',kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.user.username}')
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return (self.user.username)

class Admin(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12,unique=True)
    bio = models.TextField(blank=True)
    is_approved = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='profile_images')
    slug = models.SlugField(unique=True,blank=True)

    def get_absolute_url(self):
        return reverse('user:professor_profile_search',kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.user.username}')
        super(Admin, self).save(*args, **kwargs)

    def __str__(self):
        return (self.user.username)

