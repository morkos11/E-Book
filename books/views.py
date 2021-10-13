from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, authenticate
from django.views.generic import UpdateView
from .models import Book,BorredBook
from accounts.forms import SignupForm
from users.models import Student,Admin


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('account/signUp/complete-data')
    else:
        form = SignupForm()
    if request.user.is_authenticated:
        student = Student.objects.filter(user=request.user).exists()
        admin = Admin.objects.filter(user=request.user).exists()
        if student :
            student_slug = Student.objects.get(user=request.user)
            student_slug = student_slug.slug
        else:
            student_slug = None

        if admin :
            admin_slug = Admin.objects.get(user=request.user)
            admin_slug = admin_slug.slug
        else:
            admin_slug = None
        books = Book.objects.all()
        for book in books:
            book.check_date()
        context = {
            'form': form,
            'books': books,
            'student': student,
            'admin': admin,
            'student_slug': student_slug,
            'admin_slug': admin_slug,
        }
    else:
        books = Book.objects.all()
        context = {
            'form':form,
            'books':books,
        }

    return render(request,'index.html',context)
def book_book(request,id):
    book = get_object_or_404(Book,id=id)
    if request.method == 'POST':
        book.return_date = request.POST['return_date']
        book.is_borred = True
        book.save()
        borred_book = BorredBook(user=request.user,book=book)
        borred_book.save()

        return redirect('/')
    content = {'book':book}
    return render(request,'BookBook.html',content)
def return_book(request,id):
    if request.method == 'POST':
        book = get_object_or_404(Book,id=id)
        book.is_borred = False
        book.return_date = None
        book.save()
        borred_book = BorredBook.objects.get(book=book)
        borred_book.delete()

        return redirect('/')
    return render(request,'return_book.html')
def delete_book(request,id):
    book = get_object_or_404(Book,id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('/')
    content = {
        'book':book
    }
    return render(request,'delete_book.html',content)


class UpdateBook(UpdateView):
    model = Book
    template_name = 'update_book.html'
    fields = ['name', 'cover','book_file','book_desc']
    success_url = '/'


