from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('<slug>',views.student_profile,name='student_profile'),
    path('update-student/<slug>', views.UpdateStudent.as_view(), name='update_student'),
    path('admin/<slug>',views.admin_profile,name='admin_profile'),
    path('admin/<slug>/show-students',views.all_students,name='show_students'),
    path('admin/search-student/',views.search_student,name='search_student'),
    path('admin/<slug>/show-books',views.all_books,name='show_books'),
    path('admin/<slug>/show-borred-books',views.all_borred_books,name='show_borred_books'),


    path('update-admin/<slug>', views.UpdateAdmin.as_view(), name='update_admin'),
    path('admin/<slug>/add-book', views.CreateBook.as_view(), name='add_book'),
]