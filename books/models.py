from django.db import models
from django.contrib.auth.models import User
import time

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=35)
    cover = models.ImageField(upload_to='books-images')
    book_file = models.FileField(upload_to='books-files')
    book_desc = models.TextField()
    is_borred = models.BooleanField(default=False)
    return_date = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.name

    def check_date(self,*args,**kwargs):
        today_date = time.strftime("%Y-%m-%d")
        if today_date == str(self.return_date):
            self.is_borred = False
        super(Book,self).save(*args,**kwargs)

class UserInfo(models.Model):
    CHOICES = (
        ('Admin','Admin'),
        ('Student','Student')
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    user_type = models.CharField(max_length=25,choices=CHOICES)

    def __str__(self):
        return (self.user.username)

class BorredBook(models.Model):
    book = models.OneToOneField(Book,on_delete=models.CASCADE)
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)

    def __str__(self):
        return (self.book.name+self.user.user.username)

