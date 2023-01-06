from django.urls import path
from .views import *
urlpatterns=[
    path('books/',get_books_page,name='books'),
    path('books/<int:id>',get_book_details,name='book-details'),
]