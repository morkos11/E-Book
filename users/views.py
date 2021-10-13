from django.shortcuts import render,get_object_or_404,redirect
from .models import Student,Admin
from django.views.generic import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from books.models import BorredBook,Book

# Create your views here.

def student_profile(request,slug):
    student = get_object_or_404(Student,slug=slug)
    books = BorredBook.objects.filter(user=request.user).exists()
    if books:
        books_items = BorredBook.objects.all().filter(user=request.user)
    else:
        books_items = None
    content = {
        'student':student,
        'books':books,
        'books_items':books_items
    }
    return render(request,'profiles/student_profile.html',content)
def admin_profile(request,slug):
    admin = get_object_or_404(Admin,slug=slug)
    content = {
        'admin':admin,

    }
    return render(request,'profiles/admin_profile.html',content)
def all_students(request,slug):
    students = Student.objects.all()
    content = {'students':students}
    return render(request,'show_students.html',content)
def all_books(request,slug):
    books = Book.objects.all()
    content = {'books':books}
    return render(request,'show_books.html',content)

def all_borred_books(request,slug):
    books = Book.objects.all().filter(is_borred=True)
    content = {'books':books}
    return render(request,'show_borred_books.html',content)

class UpdateStudent(UpdateView):
    model = Student
    template_name = 'profiles/update_student.html'
    fields = ['phone_number','profile_pic','bio']
    success_url = '/'
class UpdateAdmin(UpdateView):
    model = Admin
    template_name = 'profiles/update_admin.html'
    fields = ['phone_number','profile_pic','bio']
    success_url = '/'
class CreateBook(CreateView):
    model = Book
    template_name = 'add_book.html'
    fields = ['name', 'cover','book_file','book_desc']
    success_url = '/'


