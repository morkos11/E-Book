from django.db import models
from django.contrib.auth.models import User
import time

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=35,unique=True)
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
            borred_book = BorredBook.objects.get(book__name=self.name)
            borred_book.delete()
        super(Book,self).save(*args,**kwargs)

class BorredBook(models.Model):
    book = models.OneToOneField(Book,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return (self.book.name+'_'+self.user.username)

