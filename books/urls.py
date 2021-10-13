from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('<id>',views.book_book,name='book_book'),
    path('return-book/<id>',views.return_book,name='return_book'),
    path('admin/delete-book/<id>',views.delete_book,name='delete_book'),


    path('admin/update-book/<int:pk>',views.UpdateBook.as_view(),name='update_book'),

]