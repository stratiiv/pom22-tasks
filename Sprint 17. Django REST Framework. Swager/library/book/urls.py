from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'book', BookViewSet,basename="book")
urlpatterns=[
    path('api/v1/',include(router.urls)),
    path('books/',get_books_page,name='books'),
    path('books/<int:id>/',get_book_details,name='book-details'),
    path('books/filter/',get_filtered_books,name='filter-books'),
    path('books/add/',get_add_book,name='add-book')
]