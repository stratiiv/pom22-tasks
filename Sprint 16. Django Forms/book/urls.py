from django.urls import path
from .views import *
urlpatterns=[
    path('books/',get_book_list,name='books'),
    path('books/<int:pk>/',BookDetailView.as_view(),name='book-details'),
    path('books/filter/',get_filtered_books,name='filter-books'),
    path('books/add/',get_add_book,name='add-book')
]