from django.contrib import admin
from .models import Book, UserInfo, BorredBook
# Register your models here.
admin.site.register(Book)
admin.site.register(UserInfo)
admin.site.register(BorredBook)